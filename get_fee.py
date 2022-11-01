import sys
from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.bitkub.com/fee/cryptocurrency"
    res = requests.request("GET", url)
    docs = BeautifulSoup(res.text, "html.parser")
    for i in docs.find_all("div"):
        txt = (i.previous).replace("\n", "")
        print(txt)

if __name__ == "__main__":
    main()
    sys.exit(0)