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
    symbols(token)
    logout(token)
