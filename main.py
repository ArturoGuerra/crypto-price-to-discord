#!/usr/bin/env python3

import requests

class WebHook:
    def __init__(self, hook, url, currency):
        self.hook = hook
        self.url = url
        self.currency = currency

    def get(self):
        return requests.get(self.url).json()

    def post(self, data):
        requests.post(self.hook, data=data)

cryptocompare = [
    WebHook("", "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD", "ETH"),
    WebHook("", "https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=USD", "BCH"),
    WebHook("", "https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD", "LTC"),
    WebHook("", "https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD", "XMR"),
    WebHook("", "https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD", "XRP"),
    WebHook("", "https://min-api.cryptocompare.com/data/price?fsym=XLM&tsyms=USD", "XLM"),
    WebHook("", "https://min-api.cryptocompare.com/data/price?fsym=ZEC&tsyms=USD", "ZEC"),
    WebHook("", "https://min-api.cryptocompare.com/data/price?fsym=WAX&tsyms=USD", "WAX")
]

for hook in cryptocompare:
    data = hook.get()
    data = data["USD"]
    content = {
        "content": f"{hook.currency} price in USD is currently at {str(data)}"
    }

    hook.post(content)

btchook = WebHook("", "https://api.coindesk.com/v1/bpi/currentprice/BTC.json", "BTC")
data = btchook.get()
data = data["bpi"]["USD"]["rate"]
content = {
    "content": "{btchook.currency} price is currently at ${data} USD"
}
hook.post(content)
