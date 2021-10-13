import requests
import bs4
from bs4 import BeautifulSoup as bs
import datetime
import time
from itertools import count
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

plt.style.use("fivethirtyeight")

symbol = str(input("Enter Stock Symbol: \n"))
symbol = symbol.upper()

print()

def price():
    r = requests.get(f"https://in.finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch")
    soup = bs(r.text, "lxml")
    price = soup.find("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find("span").text
    #print(f"{now} - {price.text}")
    return price

x = []
y = []

plt.title("{symbol}")

def animate(i):
    p = price()
    now = time.strftime("%H:%M:%S")     #24_hour   
    x.append(now)
    y.append(p)
    y.sort()
    plt.cla()
    plt.xticks(rotation=90)
    plt.xticks(size=8)
    plt.yticks(size=8)
    plt.plot(x, y)
    plt.tight_layout()
    #print(f"{now} - {p}")

def main():
    now = time.strftime("%H:%M:%S")    #24_hour
    ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
    plt.show()

try:
    while True:
        main()

except KeyboardInterrupt:
    print()
except AttributeError:
    print(f"No Stock Found With Symbol {symbol}")
