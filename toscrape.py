import json
import random
import time

import apify
from lxml import html
import requests


import apify

async def main():
    apify.utils.log.info("START CRAWLER")
    input_path = os.getenv('APIFY_INPUT_KEY', 'INPUT.json')
    with open(input_path, 'r') as input_file:
        input_data = json.load(input_file)
    url = input_data.get('url', 'http://quotes.toscrape.com')
    apify.utils.log.info(f'req to: "{url}"')
    xp_top_ten_tags = '//h2[contains(text(),"Top")]/..//a[contains(@href,"/tag/")]'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es-AR,es;q=0.9',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    res = requests.get(url, headers=headers, verify=False)
    tree = html.fromstring(res.text)
    els = tree.xpath(xp_top_ten_tags)
    assert els
    apify.utils.log.info(f'Total tags: {len(els)}')
    results = {}
    for el in els:
        tag = el.text
        href = el.attrib['href']
        apify.utils.log.info(f'Tag "{tag}"')
        results[tag] = url+href
    apify.utils.log.info(f"results = {json.dumps(results)}")
    with open('OUTPUT.json', 'w') as output_file:
        json.dump(results, output_file)
    await apify.push_data(results)    
    apify.utils.log.info("END CRAWLER")


if __name__ == '__main__':
    main()