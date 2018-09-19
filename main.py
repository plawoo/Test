import urllib.request
import sqlite3
import json
import jsonpath as jsonpath
import requests
import execjs


# 解析google的token值
class Py4Js:

    def __init__(self):
        self.ctx = execjs.compile(""" 
        function TL(a) { 
        var k = ""; 
        var b = 406644; 
        var b1 = 3293161072; 
        var jd = "."; 
        var $b = "+-a^+6"; 
        var Zb = "+-3^+b+-f"; 

        for (var e = [], f = 0, g = 0; g < a.length; g++) { 
            var m = a.charCodeAt(g); 
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
            e[f++] = m >> 18 | 240, 
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
            e[f++] = m >> 6 & 63 | 128), 
            e[f++] = m & 63 | 128) 
        } 
        a = b; 
        for (f = 0; f < e.length; f++) a += e[f], 
        a = RL(a, $b); 
        a = RL(a, Zb); 
        a ^= b1 || 0; 
        0 > a && (a = (a & 2147483647) + 2147483648); 
        a %= 1E6; 
        return a.toString() + jd + (a ^ b) 
    }; 

    function RL(a, b) { 
        var t = "a"; 
        var Yb = "+"; 
        for (var c = 0; c < b.length - 2; c += 3) { 
            var d = b.charAt(c + 2), 
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
        } 
        return a 
    } 
    """)

    def getTk(self, text):
        return self.ctx.call("TL", text)


def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    return data


def translate(content, g_tk):
    if len(content) > 4891:
        print("翻译的长度超过限制！！！")
        return

    content = urllib.parse.quote(content)

    url = "http://translate.google.cn/translate_a/single?client=t" + \
          "&sl=auto&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" + \
          "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" + \
          "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (g_tk, content)

    # 返回值是一个多层嵌套列表的字符串形式，解析起来还相当费劲，写了几个正则，发现也很不理想，
    # 后来感觉，使用正则简直就是把简单的事情复杂化，这里直接切片就Ok了
    result = open_url(url)

    end = result.find("\",")
    if end > 4:
        return result[4:end]


# 根据输入的帖子id获取评论和评论时间
def get_comment(post_id, fb_tk):
    url = "https://graph.facebook.com/v3.1/%s?fields=comments&access_token=%s" % (post_id, fb_tk)
    comment = []
    time = []
    while url:
        content = requests.get(url).text
        con = json.loads(content)
        comment = comment + jsonpath.jsonpath(con, "$..message")
        time = time + jsonpath.jsonpath(con, "$..created_time")
        url_real = jsonpath.jsonpath(con, "$..next")
        if url_real:
            url = jsonpath.jsonpath(con, "$..next")[0]
        else:
            url = 0
    else:
        comment = comment + jsonpath.jsonpath(con, "$..message")
        with open('message.txt', 'a', encoding='utf-8') as msv:
            for i in comment:
                msv.write(i)
                msv.write('\n')


def main():
    js = Py4Js()

    # while 1:
    #     content = input("输入待翻译内容：")
    #
    #     if content == 'q!':
    #         break
    #
    #     tk = js.getTk(content)
    #     translate(content, tk)
    messages = []
    count = 0
    with open('message_tr.txt', 'r', encoding='utf-8') as mf, open('message_trans.txt', 'w',
                                                                   encoding='utf-8') as mf_new:
        # 生成所有评论的列表
        for line in mf.readlines():
            messages.append(line)
        # 采用列表切片翻译实现断点继续
        while count < len(messages):
            print(messages[count])
            tk = js.getTk(messages[count])
            try:
                line_tr = translate(messages[count], tk)
                print(line_tr)
                count = count + 1
                mf_new.write(line_tr)
                mf_new.write('\n')
            except Exception as e:
                print('Error.')


# # 打开数据库
# conn = sqlite3.connect('message.db')
# print("Opened database successfully")

if __name__ == "__main__":
    main()
