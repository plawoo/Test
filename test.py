import requests
import urllib.request


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url="http://www.baidu.com", headers=headers)
response = urllib.request.urlopen(req)
data = response.read().decode('utf-8')
print(data)