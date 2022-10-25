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

        print(f"symbol: {symbol} status: {response.status_code}")

    return None

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

        payload = f'''exchange_id={exchange}&asset_id={symbol}&last_price={last}&lowest_ask={lowestAsk}&highest_bid={highestBid}&percent_change={percentChange}&base_volume={baseVolume}&quote_volume={quoteVolume}&is_frozen={isFrozen}&high_24_hr={high24hr}&low_24_hr={low24hr}&change_total={change}&prev_close={prevClose}&prev_open={prevOpen}&description={i}&is_active=true'''
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request(
            "POST", f"{api_host}/asset/lastprice", headers=headers, data=payload)

        print(f"SYNC: {symbol} Status: {response.status_code}")




def logout(token):
    payload={}
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.request("GET", f"{api_host}/auth/logout", headers=headers, data=payload)
    print(response.text)
    return None


if __name__ == "__main__":
    token = login()
    # symbols(token)
    get_bit_kub_last_price(token)
    logout(token)
