# -*- coding: utf-8 -*-
import requests as req
from bs4 import BeautifulSoup as soup
import re
import os

def get_token():
    #絶対パス取得
    path = os.path.dirname(os.path.abspath(__file__)) + "/token.txt"
    f = open(path, "r")
    t = f.readlines()[0].rstrip("\n")
    f.close()
    return t


# line notify url
lineurl = "https://notify-api.line.me/api/notify"
access_token = get_token()
headers = {'Authorization': 'Bearer ' + access_token}
# from qiita ranking
geturl = "https://qiita.com/takeharu/items/bb154a4bc198fb102ff3"


def getText():  # get Text
    tex = req.get(geturl)
    div = soup(tex.text, "html.parser").find_all("div", attrs={"class":"p-items_main"})[0]
    return div.find_all("a", href=re.compile("^(https://qiita)"))

# send message
def sendText(tex):
    payload = {'message': txt}
    req.post(lineurl, headers=headers, params=payload,)

def refix_soup(txt):
    # こんな感じで取れる
    # <a href="https://qiita.com/rexiaxm7/items/b745185f319edd1a17ab">【俺は絶対楽してやるんだ】徹底的に学習モチベーションを維持する方法</a>
    m = re.search(r'<a href="(?P<url>.*)">(?P<title>.*?)</a>', txt)
    url = m.group("url")
    title = m.group("title")
    return title + "\n" + url + "\n"

# main
t = getText()
daily = t[:10]
#weekly = t[10:]
txt = "Qiita Daily Ranking\n"
for i,x in enumerate(daily):
    txt += str(i+1)
    txt += "位:"
    txt += refix_soup(x.__str__())
sendText(txt)
#print("weekly ranking")
#for i,x in enumerate(weekly):
#    print(i+1, end="位:")
#    print(x)
# sendText(t)
