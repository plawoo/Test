# -*- coding: utf-8 -*-
import json
import jsonpath as jsonpath
import requests
import re
import sys

TK = "EAAcAZBcJBsTkBALdSZA7jnnJasFhqspDtk7lVjtLaY28fTI" \
     "m4lj6C25qSloMNh6JloWZBygvZCahYF2ZAOaoMudtkaYSZCjJoZ" \
     "AvqdiizJZByO9gaZC7ZCw6RBDHhiZAWgeef2YKnWSmEMAH9YAqjcx" \
     "UJjBHXjVnhgqtKWxbApo8fP9zWJq6zvZB8GGxOPY7AKBuwNYZD"

url = "https://graph.facebook.com/v3.1/%s?fields=comments&access_token=%s" % (id, TK)

commentList = []
while url:
    content = requests.get(url).text
    con = json.loads(content)
    commentList = commentList + jsonpath.jsonpath(con, "$..id")
    url_real = jsonpath.jsonpath(con, "$..next")
    if url_real:
        url = jsonpath.jsonpath(con, "$..next")[0]
    else:
        url = 0
else:
    commentList = commentList + jsonpath.jsonpath(con, "$..id")
    with open('id.txt', 'a', encoding='utf-8') as msv:
        for id in commentList:
            msv.write(id)
            msv.write('\n')

# messages = re.findall(r'"message": "(.*?)",', content, re.S)
# url_next = re.findall(r'"next": "(.*?)"', content, re.S)
# print(content)
# db_host = 'localhost'
# db_port = '6379'
# db_index = 0
# db_conn = redis.StrictRedis(host=db_host, port=db_port, db=db_index)
#
# for article in articles:
#
#     txt_url = 'http://www.guancha.cn' + article[0] + '.shtml'
#     a = {article[1]: txt_url}
#     print(a)
#
#     db_conn.hset('page', article[1], txt_url)
#
# db_conn.connection_pool.disconnect()


# text_response = requests.get(txt_url)
# text_response.encoding = 'utf-8'
# text_content = text_response.text
# print(BeautifulSoup(requests.get(txt_url).text))
# # print(soup.span.string)
