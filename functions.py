# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:16:00 2023

Get pokemon data from Chinese, English, and Japanese Pokemon wiki sites using
their API.
"""

import requests



def user_agent():
    headers = {
        'User-Agent': "pokepedia-data (Github: zian999)".encode()
    }
    return headers

def get_data(p1, p2):
    url = "https://wiki.xn--rckteqa2e.com/w/api.php?"
    action = "query"
    fmt = "json"
    prop = "extracts"
    title = "フシギダネ"
    res = requests.get(
        f"{url}{action}&format={fmt}&prop={prop}&titles={title}&utf=1",
        headers=user_agent()
    )
    if res.status_code == 200:
        data = res.json()
        return data
    else:
        data = None
        return data



#%% test code
url = "https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)"
url = "https://wiki.ポケモン.com/wiki/%E3%83%95%E3%82%B7%E3%82%AE%E3%83%80%E3%83%8D"
url = "https://wiki.52poke.com/wiki/%E5%A6%99%E8%9B%99%E7%A7%8D%E5%AD%90"
res = requests.get(url)
