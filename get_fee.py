import sys
from bs4 import BeautifulSoup
import requests


def main():
    obj = [
        ["AXS", "Ethereum", 0.41000000, 25],
        ["SAND", "Ethereum", 4.17000000, 25],
        ["IOST", "IOST", 1.00000000, 1],
        ["CTXC", "Cortex", 0.1, 300],
        ["JFIN", "Ethereum", 2.99000000, 25],
        ["ADA", "Cardano", 0.80000000, 20],
        ["BTC", "Bitcoin", 0.0002, 3],
        ["DOGE", "Dogecoin", 4.00000000, 2],
        ["MKR", "Ethereum", 0.00420000, 25],
        ["ENJ", "Ethereum", 8.25000000, 25],
        ["ABT", "Ethereum", 35, 25],
        ["MANA", "Ethereum", 5.52000000, 25],
        ["BAND", "Band Protocol", 0.01, 1],
        ["GLM", "Ethereum", 13.00000000, 25],
        ["FTT", "Ethereum", 0.14000000, 25],
        ["GF", "Ethereum", 10, 25],
        ["CHZ", "Ethereum", 17.00000000, 25],
        ["LYXE", "Ethereum", 1.5, 25],
        ["SOL", "Solana", 0.00800000, 5],
        ["FTM", "Fantom", 0.10000000, 5],
        ["LUNC", "Terra Classic", 70.00000000, 5],
        ["APE", "Ethereum", 0.80000000, 25],
        ["XTZ", "Tezos", 0.1, 1],
        ["SOLO", "Ripple", 1.0, 30],
        ["OP", "Optimism", 0.5, 1],
        ["KUB", "Ethereum", 2.70000000, 25],
        ["KUB", "Bitkub Chain", 0.01, 25],
        ["COMP", "Ethereum", 0.07500000, 25],
        ["XRP", "Ripple", 0.20000000, 1],
        ["ALPHA", "Ethereum", 31.00000000, 25],
        ["AAVE", "Ethereum", 0.04500000, 25],
        ["BCH", "Bitcoin Cash", 0.00080000, 3],
        ["SCRT", "Secret Network", 0.1, 1],
        ["YFI", "Ethereum", 0.00046000, 25],
        ["OMG", "Ethereum", 2.27000000, 25],
        ["KSM", "Kusama", 0.01, 1],
        ["ZRX", "Ethereum", 14.00000000, 25],
        ["DAI", "Ethereum", 10.00000000, 25],
        ["SNX", "Ethereum", 8.76000000, 25],
        ["BOBA", "Ethereum", 13.00000000, 25],
        ["GT", "Ethereum", 9.5, 25],
        ["DYDX", "Ethereum", 28.00000000, 25],
        ["TRX", "Tron", 1.0, 1],
        ["GAL", "Ethereum", 1.7600000, 25],
        ["1INCH", "Ethereum", 6.96, 25],
        ["CVC", "Ethereum", 30.00000000, 25],
        ["SIX", "Stellar", 1, 1],
        ["LTC", "Litecoin", 0.001, 4],
        ["BAT", "Ethereum", 12.00000000, 25],
        ["ZIL", "Zilliqa", 0.2, 1],
        ["DOT", "Polkadot", 0.08000000, 1],
        ["SUSHI", "Ethereum", 2.38000000, 25],
        ["BNB", "BNB Smart Chain",0.00050000, 25],
        ["SNT", "Ethereum", 130.00000000, 25],
        ["OCEAN", "Ethereum",21.00000000, 25],
        ["SGB", "Songbird", 0.01000000, 30],
        ["IMX", "Ethereum", 6.37000000, 25],
        ["ENS", "Ethereum",0.22000000, 25],
        ["GRT", "Ethereum", 44.00000000, 25],
        ["MATIC", "Polygon", 0.1, 5],
        ["HBAR", "Hedera Hashgraph",0.80000000, 1],
        ["CELO", "Celo", 0.001, 1],
        ["ALGO", "Algorand", 0.01, 1],
        ["BUSD", "BNB Smart Chain",0.5, 15],
        ["LUNA", "Terra 2.0",0.05000000, 5],
        ["ETH", "Ethereum", 0.00076800, 25],
        ["CRV", "Ethereum",4.23000000, 25],
        ["LINK", "Ethereum",0.48000000, 25],
        ["KNC", "Ethereum", 4, 25],
        ["XLM", "Stellar", 0.02, 1],
        ["BAL", "Ethereum", 0.55000000, 25],
        ["NEAR", "NEAR Protocol", 0.01, 1],
        ["POW", "Ethereum", 18.00000000, 25],
        ["USDT", "BNB Smart Chain", 0.8, 25],
        ["USDT", "Ethereum", 3.2, 25],
        ["USDC", "Ethereum", 3.20000000, 25],
        ["DON", "IOST", 0.82000000, 1],
        ["WAN", "Wanchain", 0.1, 30],
        ["UNI", "Ethereum", 0.54000000, 25],
        ["GALA", "Ethereum", 88.00000000, 25],
        ["ILV", "Ethereum", 0.05700000, 25],
        ["EXFI", "Songbird", 0.1, 30],
        ["AVAX", "Avalanche C-Chain",0.00800000, 12],
        ["LRC", "Ethereum", 23.0, 0],
        ["ATOM", "Cosmos", 0.005, 10],
        ["LDO", "Ethereum", 1.97, 25],
        ["STG", "Ethereum", 5.94, 25],
    ]

    for i in obj:
        symbol = i[0]
        network = i[1]
        fee = i[2]
        block = i[3]
        url = "http://localhost:4041/api/v1/asset/fee"
        payload = f'asset_id={symbol}&block_chain_id={network}&fee={fee}&block_previous={block}&description=-&is_active=true'
        headers = {
            'Authorization': 'Bearer TTu1t-3fXB3ryN_8X0RjoBIsO2WzhXBZFUxXGXJFcbsJg_rFNgb30ZYZhWDF',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)






if __name__ == "__main__":
    main()
    sys.exit(0)
