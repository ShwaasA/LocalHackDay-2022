import requests
import bs4
from bs4 import BeautifulSoup as bs
import datetime
import time

symbol = str(input("Enter Symbol: \n"))
symbol = symbol.upper()

print()

def stock():
    r = requests.get(f"https://in.finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch")
    soup = bs(r.text, "lxml")
    # price = soup.find("div", {"class": "My(6px) Pos(r) smartphone_Mt(6px) W(100%)"})
    price = soup.find("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    print(price)
    # print(f"{now} - {price.text}")

try:
    while True:
        now = time.strftime("%H:%M:%S")    #24_hour
        stock()
   
except KeyboardInterrupt:
    print()

