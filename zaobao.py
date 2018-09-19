#-*- coding: utf-8 -*-

import requests
import redis
from bs4 import BeautifulSoup
import re

url = 'http://www.guancha.cn/'
response = requests.get(url)
response.encoding = 'utf-8'
content = response.text

soup = BeautifulSoup(content, 'lxml')
articles = re.findall('<h4 class="module-title"><a href="(.*?).shtml" target="_blank">(.*?)</a></h4>', content, re.S)

print(response.status_code)

db_host = 'localhost'
db_port = '6379'
db_index = 0
db_conn = redis.StrictRedis(host=db_host, port=db_port, db=db_index)

for article in articles:

    txt_url = 'http://www.guancha.cn' + article[0] + '.shtml'
    a = {article[1]: txt_url}
    print(a)

    db_conn.hset('page', article[1], txt_url)

db_conn.connection_pool.disconnect()






# text_response = requests.get(txt_url)
# text_response.encoding = 'utf-8'
# text_content = text_response.text
# print(BeautifulSoup(requests.get(txt_url).text))
# # print(soup.span.string)