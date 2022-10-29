from datetime import datetime, timedelta
import requests

api_host = "http://localhost:4041/api/v1"
stable_coins = ["BUSD", "USDT", "USDC", "USD", "DAI"]


def login():
    payload = 'username=krumii.it%40gmail.com&password=admin%40local'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.request(
        "POST", f"{api_host}/auth/authorization", headers=headers, data=payload)
    return (response.json())["data"]["jwt_token"]


def symbols(token):
    ## Bitkub
    url = "https://api.bitkub.com/api/market/symbols"
    response = requests.request("GET", url)
    data = response.json()
    rn = 1
    for s in data["result"]:
        symbol = (s["symbol"])[len("THB_"):]
        description = (s["info"])[len("Thai Baht to "):]
        payload = f'asset_group_id=-&symbol={symbol}&description={description}&is_active=true'
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request(
            "POST", f"{api_host}/asset/list", headers=headers, data=payload)

        print(f"{s['id']} BITKUB==> symbol: {symbol} status: {response.status_code}")
        rn += 1

    ## satang pro
    response = requests.request("GET", f"https://satangcorp.com/api/v3/exchangeInfo")
    if response.status_code == 200:
        obj = response.json()["symbols"]
        for i in obj:
            symbol = str(i['baseAsset']).upper()
            description = str(i['baseAsset']).upper()
            payload = f'asset_group_id=-&symbol={symbol}&description={description}&is_active=true'
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            response = requests.request(
                "POST", f"{api_host}/asset/list", headers=headers, data=payload)

            print(f"{s['id']} SATANG PRO ==> symbol: {symbol} status: {response.status_code}")
            rn += 1
    return None


def get_thb_rate():
    dte = datetime.now() - timedelta(days=1)
    start_period = dte.strftime("%Y-%m-%d")
    end_period = datetime.now().strftime("%Y-%m-%d")
    url = f"https://apigw1.bot.or.th/bot/public/Stat-ReferenceRate/v2/DAILY_REF_RATE/?start_period={start_period}&end_period={end_period}"
    headers = {'X-IBM-Client-Id': 'f7379501-3434-4047-9ee9-e0b81919663b', }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    x = float(data["result"]["data"]["data_detail"][0]["rate"])
    return x


def get_gate_io_last_price(token):
    thb = get_thb_rate()
    exchange = "Gate.io"
    response = requests.request(
            "GET", f"https://api.gateio.ws/api/v4/spot/tickers")
    if response.status_code == 200:
        obj = response.json()
        for i in obj:
            symbol = (i['currency_pair'])[:(i['currency_pair']).find("_")]
            pair = (i['currency_pair'])[(i['currency_pair']).find("_") + 1:]
            try:
                isFound = stable_coins.index(pair)
                if isFound >= 0:
                    last = float(i['last'])*thb
                    lowestAsk = float(i['lowest_ask'])
                    highestBid = float(i['highest_bid'])
                    percentChange = float(i['change_percentage'])
                    baseVolume = float(i['base_volume'])
                    quoteVolume = float(i['quote_volume'])
                    isFrozen = 0  # float(obj['weightedAvgPrice'])
                    high24hr = float(i['high_24h'])
                    low24hr = float(i['low_24h'])
                    change = 0  # float(obj['priceChange'])
                    prevClose = 0  # float(obj['lastPrice'])*thb
                    prevOpen = 0  # float(obj['lastPrice'])*thb
                    payload = f"exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={symbol}_{exchange}&is_active=true"
                    headers = {
                        'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                    response = requests.request(
                        "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)
                    print(
                        f"{exchange} ==> symbol: {symbol} price: {last} status: {response.status_code}")
            except Exception as e:
                pass

def get_satang_pro_last_price(token):
    exchange = "Satang Pro"
    response = requests.request("GET", f"https://satangcorp.com/api/v3/ticker/24hr")
    if response.status_code == 200:
        obj = response.json()
        for i in obj:
            symbol = str((i['symbol'])[:len(i['symbol'])-4]).upper()
            last = float(i['lastPrice'])
            lowestAsk = float(i['askPrice'])
            highestBid = float(i['bidPrice'])
            percentChange = float(i['priceChangePercent'])
            baseVolume = float(i['volume'])
            quoteVolume = float(i['quoteVolume'])
            isFrozen = float(i['weightedAvgPrice'])
            high24hr = float(i['highPrice'])
            low24hr = float(i['lowPrice'])
            change = float(i['priceChange'])
            prevClose = float(i['lastPrice'])
            prevOpen = float(i['lastPrice'])
            payload = f"exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={symbol}_{exchange}&is_active=true"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            response = requests.request(
                "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)
            print(
                f"{exchange} ==> symbol: {symbol} price: {last} status: {response.status_code}")
        


def get_binance_last_price(token):
    thb = get_thb_rate()
    exchange = "Binance"
    response = requests.request(
        "GET", f"https://api.binance.com/api/v3/ticker/24hr")
    if response.status_code == 200:
        data = response.json()
        for i in data:
            eq = (i['symbol'])[len(i['symbol']) - 4:]
            # print(f"Symbol: {i['symbol']} sub: {eq}")
            try:
                if (stable_coins).index(eq) >= 0:
                    sym = (i['symbol'])[:(len("BUSD")-(len(i['symbol']) + 1))]
                    symbol = sym
                    last = float(i['lastPrice'])*thb
                    lowestAsk = float(i['askPrice'])*thb
                    highestBid = float(i['bidPrice'])*thb
                    percentChange = float(i['priceChangePercent'])
                    baseVolume = float(i['volume'])
                    quoteVolume = float(i['quoteVolume'])
                    isFrozen = float(i['weightedAvgPrice'])
                    high24hr = float(i['highPrice'])
                    low24hr = float(i['lowPrice'])
                    change = float(i['priceChange'])
                    prevClose = float(i['lastPrice'])*thb
                    prevOpen = float(i['lastPrice'])*thb
                    payload = f"exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={symbol}_{exchange}&is_active=true"
                    headers = {
                        'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }

                    response = requests.request(
                        "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

                    print(
                        f"{exchange} ==> symbol: {symbol} price: {last} status: {response.status_code}")

            except Exception as e:
                pass


def get_bit_kub_last_price(token):
    url = "https://api.bitkub.com/api/market/ticker"
    response = requests.request("GET", url)
    data = response.json()
    for i in data:
        obj = data[i]
        exchange = "Bitkub"
        symbol = str(i)[len("THB_"):]
        last = obj["last"]
        lowestAsk = obj["lowestAsk"]
        highestBid = obj["highestBid"]
        percentChange = obj["percentChange"]
        baseVolume = obj["baseVolume"]
        quoteVolume = obj["quoteVolume"]
        isFrozen = obj["isFrozen"]
        high24hr = obj["high24hr"]
        low24hr = obj["low24hr"]
        change = obj["change"]
        prevClose = obj["prevClose"]
        prevOpen = obj["prevOpen"]

        payload = f"exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={symbol}_{exchange}&is_active=true"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request(
            "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

        print(
            f"{exchange} ==> symbol: {symbol} price: {last} status: {response.status_code}")


def get_kucoin_last_price(token):
    thb = get_thb_rate()
    exchange = "Kucoin"
    response = requests.request(
        "GET", f"https://api.kucoin.com/api/v1/market/allTickers")
    if response.status_code == 200:
        obj = response.json()["data"]["ticker"]
        for i in obj:
            sym = i['symbol']
            symbol = sym[:(sym).find("-")]
            pair = sym[(sym).find("-") + 1:]
            try:
                if ((stable_coins).index(pair)) >= 0:
                    last = float(i['last'])*thb
                    lowestAsk = 0  # float(obj['buy'])
                    highestBid = 0  # float(obj['sell'])
                    percentChange = float(i['changeRate'])
                    baseVolume = float(i['vol'])
                    quoteVolume = float(i['volValue'])
                    isFrozen = 0  # float(obj['weightedAvgPrice'])
                    high24hr = float(i['high'])
                    low24hr = float(i['low'])
                    change = float(i['changePrice'])
                    prevClose = 0  # float(obj['lastPrice'])*thb
                    prevOpen = 0  # float(obj['lastPrice'])*thb
                    payload = f"exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={symbol}_{exchange}&is_active=true"
                    headers = {
                        'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                    response = requests.request(
                        "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)
                    print(
                        f"{exchange} ==> symbol: {symbol} price: {last} status: {response.status_code}")
            except Exception as e:
                pass

def get_ftx_last_price(token):
    thb = get_thb_rate()
    exchange = "FTX"
    response = requests.request("GET", f"https://ftx.com/api/markets")
    obj = response.json()["result"]
    for i in obj:
        name = i["name"]
        symbol = name[:name.find("/")]
        pair = name[name.find("/") + 1:]
        try:
            if (stable_coins.index(pair)) >= 0:
                last = float(i['last'])*thb
                lowestAsk = float(i['ask'])
                highestBid = float(i['bid'])
                percentChange = float(i['changeBod'])
                baseVolume = float(i['volumeUsd24h'])
                quoteVolume = float(i['quoteVolume24h'])
                isFrozen = float(i['largeOrderThreshold'])
                high24hr = float(i['priceHigh24h'])
                low24hr = float(i['priceLow24h'])
                change = float(i['change24h'])
                prevClose = 0  # float(obj['lastPrice'])*thb
                prevOpen = 0  # float(obj['lastPrice'])*thb

                payload = f"exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={symbol}_{exchange}&is_active=true"
                headers = {
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/x-www-form-urlencoded'
                }

                response = requests.request(
                    "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

                print(
                    f"{exchange} ==> symbol: {symbol} price: {last} status: {response.status_code}")

        except Exception as ex:
            pass

def get_okx_last_price(token):
    thb = get_thb_rate()
    exchange = "OKX"
    response = requests.request("GET", f"https://www.okx.com/api/v5/market/tickers?instType=SWAP")
    if response.status_code == 200:
        for i in response.json()["data"]:
            sym = i["instId"]
            symbol = sym[:sym.find("-")]
            p = sym[sym.find("-")+1:]
            pair = p[:p.find("-")]
            try:
                if (stable_coins.index(pair)) >= 0:
                    last = float(i['last'])*thb
                    lowestAsk = float(i['askPx'])
                    highestBid = float(i['bidPx'])
                    percentChange = 0  # float(obj['changeBod'])
                    baseVolume = float(i['vol24h'])
                    quoteVolume = float(i['volCcy24h'])
                    isFrozen = 0  # float(obj['largeOrderThreshold'])
                    high24hr = float(i['high24h'])
                    low24hr = float(i['low24h'])
                    change = 0  # float(obj['change24h'])
                    prevClose = 0  # float(obj['lastPrice'])*thb
                    prevOpen = 0  # float(obj['lastPrice'])*thb

                    payload = f"exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={symbol}_{exchange}&is_active=true"
                    headers = {
                        'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }

                    response = requests.request(
                        "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

                    print(
                        f"{exchange} ==> symbol: {symbol} price: {last} status: {response.status_code}")

            except Exception as e:
                print(e)
                pass

def get_coin_ex_last_price(token):
    thb = get_thb_rate()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.request(
        "GET", f"{api_host}/asset/list", headers=headers)
    asset = response.json()["data"]

    response = requests.request(
        "GET", f"https://api.coinex.com/v1/market/ticker/all")
    data = response.json()["data"]["ticker"]
    if response.status_code == 200:
        for i in asset:
            exchange = "CoinEx"
            symbol = i['symbol']
            try:
                obj = data[f"{symbol}USDT"]
                last = float(obj['last'])*thb
                lowestAsk = float(obj['buy'])
                highestBid = float(obj['sell'])
                percentChange = 0  # float(obj['changeBod'])
                baseVolume = float(obj['vol'])
                quoteVolume = float(obj['sell_amount'])
                isFrozen = 0  # float(obj['largeOrderThreshold'])
                high24hr = float(obj['high'])
                low24hr = float(obj['low'])
                change = 0  # float(obj['change24h'])
                prevClose = 0  # float(obj['lastPrice'])*thb
                prevOpen = float(obj['open'])
                payload = f"exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={symbol}_{exchange}&is_active=true"
                headers = {
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
                response = requests.request(
                    "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)
                print(
                    f"{exchange} ==> symbol: {symbol} price: {last} status: {response.status_code}")
            except Exception as e:
                pass


def get_poloniex_last_price(token):
    thb = get_thb_rate()
    exchange = "Poloniex"
    response = requests.request("GET", f"https://api.poloniex.com/markets/ticker24h")
    if response.status_code == 200:
        obj = response.json()
        for i in obj:
            sym = i['displayName']
            symbol = sym[:sym.find("/")]
            pair = sym[sym.find("/") + 1:]
            try:
                if (stable_coins.index(pair)) >= 0:
                    last = float(i['close'])*thb
                    lowestAsk = 0  # float(obj['askPrice'])*thb
                    highestBid = 0  # float(obj['bidPrice'])*thb
                    percentChange = 0  # float(obj['priceChangePercent'])
                    baseVolume = float(i['quantity'])
                    quoteVolume = float(i['amount'])
                    isFrozen = 0  # float(obj['weightedAvgPrice'])
                    high24hr = float(i['high'])
                    low24hr = float(i['low'])
                    change = 0  # float(obj['priceChange'])
                    prevClose = float(i['close'])
                    prevOpen = float(i['open'])

                    payload = f"exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={symbol}_{exchange}&is_active=true"
                    headers = {
                        'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }

                    response = requests.request(
                        "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

                    print(
                        f"{exchange} ==> symbol: {symbol} price: {last} status: {response.status_code}")
            except Exception as e:
                pass

def get_mexc_last_price(token):
    thb = get_thb_rate()
    exchange = "MEXC"
    response = requests.request(
        "GET", f"https://www.mexc.com/open/api/v2/market/ticker")
    if response.status_code == 200:
        obj = response.json()["data"]
        for i in obj:
            sym = i['symbol']
            symbol = sym[:(sym).find("_")]
            pair = sym[(sym).find("_")+1:]
            try:
                if (stable_coins.index(pair)) >= 0:
                    last = float(i['last'])*thb
                    lowestAsk = float(i['ask'])
                    highestBid = float(i['bid'])
                    percentChange = float(i['change_rate'])
                    baseVolume = float(i['volume'])
                    quoteVolume = float(i['amount'])
                    isFrozen = 0  # float(obj['weightedAvgPrice'])
                    high24hr = float(i['high'])
                    low24hr = float(i['low'])
                    change = float(i['change_rate'])
                    prevClose = float(i['last'])*thb
                    prevOpen = float(i['open'])*thb

                    payload = f"exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={symbol}_{exchange}&is_active=true"
                    headers = {
                        'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                    response = requests.request(
                        "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)
                    print(f"{exchange} ==> symbol: {symbol} price: {last} status: {response.status_code}")
            except Exception as e:
                pass


def logout(token):
    payload = {}
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.request(
        "GET", f"{api_host}/auth/logout", headers=headers, data=payload)
    print(response.text)
    return None


if __name__ == "__main__":
    token = login()
    symbols(token)
    print(f"1.------------- BITKUB -----------------")
    get_bit_kub_last_price(token)
    print(f"2.------------- COINEX -----------------")
    get_coin_ex_last_price(token)
    print(f"3.------------- BINANCE -----------------")
    get_binance_last_price(token)
    print(f"4.------------- SATANG PRO -----------------")
    get_satang_pro_last_price(token)
    print(f"5.------------- Gate.io -----------------")
    get_gate_io_last_price(token)
    print(f"6.------------- KUCOIN -----------------")
    get_kucoin_last_price(token)
    print(f"7.------------- FTX -----------------")
    get_ftx_last_price(token)
    print(f"8.------------- OKX -----------------")
    get_okx_last_price(token)
    print(f"9.------------- POLONIX -----------------")
    get_poloniex_last_price(token)
    print(f"10.------------- MEXC -----------------")
    get_mexc_last_price(token)
    logout(token)
