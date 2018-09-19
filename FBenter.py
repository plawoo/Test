# -*-coding:utf-8-*-
import requests

# 此处为用户所要登陆的网站链接
url = 'https://www.facebook.com/'
# 浏览器访问网站的cookie信息
cookie = {"Cookie": "sb=tLxfW_RbKIH6B8XRtfvoK5Lt; "
                    "datr=tLxfW_d4DRBkHz_Gflm2J6jX; pl=n; locale=en_US; "
                    "c_user=100025090593254; xs=19%3A78sCbRBriFyePA%3A2%3A1536886461%3A6407%3A7968;"
                    " fr=0yqxGH8gkj8FyZFqh.AWWcs9AU5LcGxYtX6BE4-qovS-o.BbX7y0.C0.AAA.0.0.Bbmwa8.AWXh23Wc; "
                    "spin=r.4310513_b.trunk_t.1536886462_s.1_v.2_; wd=1920x430; presence=EDvF3EtimeF1536973"
                    "756EuserFA21B25090593254A2EstateFDt3F_5b_5dG536973756512CEchFDp_5f1B25090593254F31CC; "
                    "act=1536973757278%2F75"}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/68.0.3440.75 Safari/537.36'}
# requests请求，获取登录网站页面
html = requests.get(url, headers=headers, cookies=cookie).content
print(html)
