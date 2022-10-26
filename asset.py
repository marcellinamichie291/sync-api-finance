from datetime import datetime, timedelta
import requests

api_host = "http://localhost:4041/api/v1"


def login():
    payload = 'username=krumii.it%40gmail.com&password=admin%40local'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.request(
        "POST", f"{api_host}/auth/authorization", headers=headers, data=payload)
    return (response.json())["data"]["jwt_token"]


def symbols(token):
    url = "https://api.bitkub.com/api/market/symbols"
    response = requests.request("GET", url)
    data = response.json()
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

        # print(f"symbol: {symbol} status: {response.status_code}")

    # response = requests.request(
    #     "GET", "https://api.gateio.ws/api/v4/spot/tickers")
    # for i in response.json():
    #     symbol = (i['currency_pair'])[:(i['currency_pair']).find('_')]
    #     description = symbol
    #     payload = f'asset_group_id=-&symbol={symbol}&description={description}&is_active=true'
    #     headers = {
    #         'Authorization': f'Bearer {token}',
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }

    #     response = requests.request(
    #         "POST", f"{api_host}/asset/list", headers=headers, data=payload)
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
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.request(
        "GET", f"{api_host}/asset/list", headers=headers, data={})
    for i in response.json()["data"]:
        response = requests.request(
            "GET", f"https://api.gateio.ws/api/v4/spot/tickers?currency_pair={i['symbol']}_USDT")
        if response.status_code == 200:
            obj = response.json()[0]
            exchange = "Gate.io"
            symbol = i['symbol']
            last = float(obj['last'])*thb
            lowestAsk = float(obj['lowest_ask'])*thb
            highestBid = float(obj['highest_bid'])*thb
            percentChange = float(obj['change_percentage'])*thb
            baseVolume = float(obj['base_volume'])*thb
            quoteVolume = float(obj['quote_volume'])*thb
            isFrozen = 0  # float(obj['weightedAvgPrice'])*thb
            high24hr = float(obj['high_24h'])*thb
            low24hr = float(obj['low_24h'])*thb
            change = 0  # float(obj['priceChange'])*thb
            prevClose = 0  # float(obj['lastPrice'])*thb
            prevOpen = 0  # float(obj['lastPrice'])*thb

            payload = f'''exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={i['symbol']}_GATE.IO&is_active=true'''
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            response = requests.request(
                "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

            print(
                f"GATE.IO ==> symbol: {i['symbol']} price: {last} status: {response.status_code}")


def get_satang_pro_last_price(token):
    # thb = get_thb_rate()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.request(
        "GET", f"{api_host}/asset/list", headers=headers, data={})
    for i in response.json()["data"]:
        response = requests.request(
            "GET", f"https://satangcorp.com/api/v3/ticker/24hr?symbol={(i['symbol']).lower()}_thb")
        if response.status_code == 200:
            obj = response.json()
            exchange = "Satang Pro"
            symbol = i['symbol']
            last = float(obj['lastPrice'])
            lowestAsk = float(obj['askPrice'])
            highestBid = float(obj['bidPrice'])
            percentChange = float(obj['priceChangePercent'])
            baseVolume = float(obj['volume'])
            quoteVolume = float(obj['quoteVolume'])
            isFrozen = float(obj['weightedAvgPrice'])
            high24hr = float(obj['highPrice'])
            low24hr = float(obj['lowPrice'])
            change = float(obj['priceChange'])
            prevClose = float(obj['lastPrice'])
            prevOpen = float(obj['lastPrice'])

            payload = f'''exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={i['symbol']}_SATANG_PRO&is_active=true'''
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            response = requests.request(
                "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

            print(
                f"Satang Pro ==> symbol: {i['symbol']} price: {last} status: {response.status_code}")


def get_binance_last_price(token):
    thb = get_thb_rate()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.request(
        "GET", f"{api_host}/asset/list", headers=headers, data={})
    for i in response.json()["data"]:
        response = requests.request(
            "GET", f"https://api.binance.com/api/v3/ticker/24hr?symbol={i['symbol']}BUSD")
        if response.status_code == 200:
            obj = response.json()
            exchange = "Binance"
            symbol = i['symbol']
            last = float(obj['lastPrice'])*thb
            lowestAsk = float(obj['askPrice'])*thb
            highestBid = float(obj['bidPrice'])*thb
            percentChange = float(obj['priceChangePercent'])*thb
            baseVolume = float(obj['volume'])*thb
            quoteVolume = float(obj['quoteVolume'])*thb
            isFrozen = float(obj['weightedAvgPrice'])*thb
            high24hr = float(obj['highPrice'])*thb
            low24hr = float(obj['lowPrice'])*thb
            change = float(obj['priceChange'])*thb
            prevClose = float(obj['lastPrice'])*thb
            prevOpen = float(obj['lastPrice'])*thb

            payload = f'''exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={i['symbol']}_BINANCE&is_active=true'''
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            response = requests.request(
                "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

            print(
                f"BINANCE ==> symbol: {i['symbol']} price: {last} status: {response.status_code}")


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

        payload = f'''exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={symbol}_BITKUB&is_active=true'''
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request(
            "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

        print(
            f"BITKUB ==> symbol: {symbol} lastprice: {last} Status: {response.status_code}")


def get_kucoin_last_price(token):
    thb = get_thb_rate()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.request(
        "GET", f"{api_host}/asset/list", headers=headers, data={})
    for i in response.json()["data"]:
        response = requests.request(
            "GET", f"https://api.kucoin.com/api/v1/market/stats?symbol={i['symbol']}-USDT")
        if response.status_code == 200:
            obj = response.json()["data"]
            if obj['last'] != None:
                exchange = "Kucoin"
                symbol = i['symbol']
                last = float(obj['last'])*thb
                lowestAsk = 0  # float(obj['buy'])*thb
                highestBid = 0  # float(obj['sell'])*thb
                percentChange = float(obj['changeRate'])*thb
                baseVolume = float(obj['vol'])*thb
                quoteVolume = float(obj['volValue'])*thb
                isFrozen = 0  # float(obj['weightedAvgPrice'])*thb
                high24hr = float(obj['high'])*thb
                low24hr = float(obj['low'])*thb
                change = float(obj['changePrice'])*thb
                prevClose = 0  # float(obj['lastPrice'])*thb
                prevOpen = 0  # float(obj['lastPrice'])*thb

                payload = f'''exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={i['symbol']}_KUCOIN&is_active=true'''
                headers = {
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/x-www-form-urlencoded'
                }

                response = requests.request(
                    "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

                print(
                    f"KUCOIN ==> symbol: {i['symbol']} price: {last} status: {response.status_code}")


def get_ftx_last_price(token):
    thb = get_thb_rate()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.request(
        "GET", f"{api_host}/asset/list", headers=headers, data={})
    for i in response.json()["data"]:
        response = requests.request(
            "GET", f"https://ftx.com/api/markets/{i['symbol']}/USDT")
        if response.status_code == 200:
            obj = response.json()["result"]
            if obj['last'] != None:
                exchange = "FTX"
                symbol = i['symbol']
                last = float(obj['last'])*thb
                lowestAsk = float(obj['ask'])*thb
                highestBid = float(obj['bid'])*thb
                percentChange = float(obj['changeBod'])*thb
                baseVolume = float(obj['volumeUsd24h'])*thb
                quoteVolume = float(obj['quoteVolume24h'])*thb
                isFrozen = float(obj['largeOrderThreshold'])*thb
                high24hr = float(obj['priceHigh24h'])*thb
                low24hr = float(obj['priceLow24h'])*thb
                change = float(obj['change24h'])*thb
                prevClose = 0  # float(obj['lastPrice'])*thb
                prevOpen = 0  # float(obj['lastPrice'])*thb

                payload = f'''exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={i['symbol']}_FTX&is_active=true'''
                headers = {
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/x-www-form-urlencoded'
                }

                response = requests.request(
                    "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

                print(
                    f"FTX ==> symbol: {i['symbol']} price:{last} status: {response.status_code}")


def get_okx_last_price(token):
    thb = get_thb_rate()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.request(
        "GET", f"{api_host}/asset/list", headers=headers, data={})
    for i in response.json()["data"]:
        # print(f"https://www.okx.com/api/v5/market/ticker?instId={i['symbol']}-USD-SWAP")
        response = requests.request(
            "GET", f"https://www.okx.com/api/v5/market/ticker?instId={i['symbol']}-USD-SWAP")
        if response.status_code == 200:
            if response.json()["code"] == "0":
                obj = response.json()["data"][0]
                if obj['last'] != None:
                    exchange = "OKX"
                    symbol = i['symbol']
                    last = float(obj['last'])*thb
                    lowestAsk = float(obj['askPx'])*thb
                    highestBid = float(obj['bidPx'])*thb
                    percentChange = 0  # float(obj['changeBod'])*thb
                    baseVolume = float(obj['vol24h'])*thb
                    quoteVolume = float(obj['volCcy24h'])*thb
                    isFrozen = 0  # float(obj['largeOrderThreshold'])*thb
                    high24hr = float(obj['high24h'])*thb
                    low24hr = float(obj['low24h'])*thb
                    change = 0  # float(obj['change24h'])*thb
                    prevClose = 0  # float(obj['lastPrice'])*thb
                    prevOpen = 0  # float(obj['lastPrice'])*thb

                    payload = f'''exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={i['symbol']}_OKX&is_active=true'''
                    headers = {
                        'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }

                    response = requests.request(
                        "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

                    print(
                        f"OKX ==> symbol: {i['symbol']} price:{last} status: {response.status_code}")


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
    print(f"------------- BITKUB -----------------")
    get_bit_kub_last_price(token)
    print(f"------------- BINANCE -----------------")
    get_binance_last_price(token)
    print(f"------------- SATANG PRO -----------------")
    get_satang_pro_last_price(token)
    print(f"------------- Gate.io -----------------")
    get_gate_io_last_price(token)
    print(f"------------- KUCOIN -----------------")
    get_kucoin_last_price(token)
    print(f"------------- FTX -----------------")
    get_ftx_last_price(token)
    print(f"------------- OKX -----------------")
    get_okx_last_price(token)
    symbols(token)
    logout(token)
