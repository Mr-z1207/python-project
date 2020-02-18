import os

import requests
import parsel

url = 'https://www.vmgirls.com/'
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
html_str = requests.get(url, headers=headers).text

html = parsel.Selector(html_str)
media_a_url = html.css(".media a::attr(href)").getall()

n = 1

os.mkdir('C:/Users/14360/Desktop/美女')
os.chdir('C:/Users/14360/Desktop/美女')
for href in media_a_url:
    html_str = requests.get(href, headers=headers).text
    html = parsel.Selector(html_str)
    src = html.css(".nc-light-gallery a::attr(href)").getall()
    for data in src:
        img = requests.get(data, headers=headers)
        with open('%s.jpg' % n, 'wb') as file:
            file.write(img.content)
        n = n + 1
