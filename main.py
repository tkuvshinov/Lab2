import requests
import json
import time


def getinfo():
    return requests.get("https://blockchain.info/ru/ticker").text


answer = input("Введите валюту: ")
while True:
    d = json.loads(getinfo())
    d1 = d[answer]
    print(d1["buy"])
    time.sleep(5)
