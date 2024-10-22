import json
import random
import time

import requests
from lxml import html

xp_top_ten_tags = '//h2[contains(text(),"Top")]/..//a[contains(@href,"/tag/")]'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'es-AR,es;q=0.9',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

BASE_URL = 'http://quotes.toscrape.com'
res = requests.get(BASE_URL, headers=headers, verify=False)
tree = html.fromstring(res.text)
els = tree.xpath(xp_top_ten_tags)
assert els
tag_dict = {}
for el in els:
    tag = el.text
    href = el.attrib['href']
    tag_dict[tag] = BASE_URL+href

print(tag_dict)
