import sys
from bs4 import BeautifulSoup
import requests


def main():
    obj = [
        ["AXS", "Ethereum", 0.41000000, 25, "Bitkub"],
        ["SAND", "Ethereum", 4.17000000, 25, "Bitkub"],
        ["IOST", "IOST", 1.00000000, 1, "Bitkub"],
        ["CTXC", "Cortex", 0.1, 300, "Bitkub"],
        ["JFIN", "Ethereum", 2.99000000, 25, "Bitkub"],
        ["ADA", "Cardano", 0.80000000, 20, "Bitkub"],
        ["BTC", "Bitcoin", 0.0002, 3, "Bitkub"],
        ["DOGE", "Dogecoin", 4.00000000, 2, "Bitkub"],
        ["MKR", "Ethereum", 0.00420000, 25, "Bitkub"],
        ["ENJ", "Ethereum", 8.25000000, 25, "Bitkub"],
        ["ABT", "Ethereum", 35, 25, "Bitkub"],
        ["MANA", "Ethereum", 5.52000000, 25, "Bitkub"],
        ["BAND", "Band Protocol", 0.01, 1, "Bitkub"],
        ["GLM", "Ethereum", 13.00000000, 25, "Bitkub"],
        ["FTT", "Ethereum", 0.14000000, 25, "Bitkub"],
        ["GF", "Ethereum", 10, 25, "Bitkub"],
        ["CHZ", "Ethereum", 17.00000000, 25, "Bitkub"],
        ["LYXE", "Ethereum", 1.5, 25, "Bitkub"],
        ["SOL", "Solana", 0.00800000, 5, "Bitkub"],
        ["FTM", "Fantom", 0.10000000, 5, "Bitkub"],
        ["LUNC", "Terra Classic", 70.00000000, 5, "Bitkub"],
        ["APE", "Ethereum", 0.80000000, 25, "Bitkub"],
        ["XTZ", "Tezos", 0.1, 1, "Bitkub"],
        ["SOLO", "Ripple", 1.0, 30, "Bitkub"],
        ["OP", "Optimism", 0.5, 1, "Bitkub"],
        ["KUB", "Ethereum", 2.70000000, 25, "Bitkub"],
        ["KUB", "Bitkub Chain", 0.01, 25, "Bitkub"],
        ["COMP", "Ethereum", 0.07500000, 25, "Bitkub"],
        ["XRP", "Ripple", 0.20000000, 1, "Bitkub"],
        ["ALPHA", "Ethereum", 31.00000000, 25, "Bitkub"],
        ["AAVE", "Ethereum", 0.04500000, 25, "Bitkub"],
        ["BCH", "Bitcoin Cash", 0.00080000, 3, "Bitkub"],
        ["SCRT", "Secret Network", 0.1, 1, "Bitkub"],
        ["YFI", "Ethereum", 0.00046000, 25, "Bitkub"],
        ["OMG", "Ethereum", 2.27000000, 25, "Bitkub"],
        ["KSM", "Kusama", 0.01, 1, "Bitkub"],
        ["ZRX", "Ethereum", 14.00000000, 25, "Bitkub"],
        ["DAI", "Ethereum", 10.00000000, 25, "Bitkub"],
        ["SNX", "Ethereum", 8.76000000, 25, "Bitkub"],
        ["BOBA", "Ethereum", 13.00000000, 25, "Bitkub"],
        ["GT", "Ethereum", 9.5, 25, "Bitkub"],
        ["DYDX", "Ethereum", 28.00000000, 25, "Bitkub"],
        ["TRX", "Tron", 1.0, 1, "Bitkub"],
        ["GAL", "Ethereum", 1.7600000, 25, "Bitkub"],
        ["1INCH", "Ethereum", 6.96, 25, "Bitkub"],
        ["CVC", "Ethereum", 30.00000000, 25, "Bitkub"],
        ["SIX", "Stellar", 1, 1, "Bitkub"],
        ["LTC", "Litecoin", 0.001, 4, "Bitkub"],
        ["BAT", "Ethereum", 12.00000000, 25, "Bitkub"],
        ["ZIL", "Zilliqa", 0.2, 1, "Bitkub"],
        ["DOT", "Polkadot", 0.08000000, 1, "Bitkub"],
        ["SUSHI", "Ethereum", 2.38000000, 25, "Bitkub"],
        ["BNB", "BNB Smart Chain",0.00050000, 25, "Bitkub"],
        ["SNT", "Ethereum", 130.00000000, 25, "Bitkub"],
        ["OCEAN", "Ethereum",21.00000000, 25, "Bitkub"],
        ["SGB", "Songbird", 0.01000000, 30, "Bitkub"],
        ["IMX", "Ethereum", 6.37000000, 25, "Bitkub"],
        ["ENS", "Ethereum",0.22000000, 25, "Bitkub"],
        ["GRT", "Ethereum", 44.00000000, 25, "Bitkub"],
        ["MATIC", "Polygon", 0.1, 5, "Bitkub"],
        ["HBAR", "Hedera Hashgraph",0.80000000, 1, "Bitkub"],
        ["CELO", "Celo", 0.001, 1, "Bitkub"],
        ["ALGO", "Algorand", 0.01, 1, "Bitkub"],
        ["BUSD", "BNB Smart Chain",0.5, 15, "Bitkub"],
        ["LUNA", "Terra 2.0",0.05000000, 5, "Bitkub"],
        ["ETH", "Ethereum", 0.00076800, 25, "Bitkub"],
        ["CRV", "Ethereum",4.23000000, 25, "Bitkub"],
        ["LINK", "Ethereum",0.48000000, 25, "Bitkub"],
        ["KNC", "Ethereum", 4, 25, "Bitkub"],
        ["XLM", "Stellar", 0.02, 1, "Bitkub"],
        ["BAL", "Ethereum", 0.55000000, 25, "Bitkub"],
        ["NEAR", "NEAR Protocol", 0.01, 1, "Bitkub"],
        ["POW", "Ethereum", 18.00000000, 25, "Bitkub"],
        ["USDT", "BNB Smart Chain", 0.8, 25, "Bitkub"],
        ["USDT", "Ethereum", 3.2, 25, "Bitkub"],
        ["USDC", "Ethereum", 3.20000000, 25, "Bitkub"],
        ["DON", "IOST", 0.82000000, 1, "Bitkub"],
        ["WAN", "Wanchain", 0.1, 30, "Bitkub"],
        ["UNI", "Ethereum", 0.54000000, 25, "Bitkub"],
        ["GALA", "Ethereum", 88.00000000, 25, "Bitkub"],
        ["ILV", "Ethereum", 0.05700000, 25, "Bitkub"],
        ["EXFI", "Songbird", 0.1, 30, "Bitkub"],
        ["AVAX", "Avalanche C-Chain",0.00800000, 12, "Bitkub"],
        ["LRC", "Ethereum", 23.0, 0, "Bitkub"],
        ["ATOM", "Cosmos", 0.005, 10, "Bitkub"],
        ["LDO", "Ethereum", 1.97, 25, "Bitkub"],
        ["STG", "Ethereum", 5.94, 25, "Bitkub"],
    ]

    for i in obj:
        symbol = i[0]
        network = i[1]
        fee = i[2]
        block = i[3]
        description = i[4]
        url = "http://localhost:4041/api/v1/asset/fee"
        payload = f'asset_id={symbol}&block_chain_id={network}&fee={fee}&block_previous={block}&description={description}&is_active=true'
        headers = {
            'Authorization': 'Bearer enjtpZn4gVX8yCYKwZHWxOmo9-cQusziOfl60xgXNG2Wzzh6XM7VpXRaqpQt',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(
            f"Symbol: {symbol} Network: {network} Description: {description} Status: {response.status_code}")






if __name__ == "__main__":
    main()
    sys.exit(0)
