# -*- coding: utf-8 -*-


import mechanicalsoup
from bs4 import BeautifulSoup

browser= mechanicalsoup.Browser()

def url_crawling(argUrl,argForm):
    global arr_url
    arr_url = list()

    source = browser.get(argUrl)
    soup = source.soup.findAll(argForm)     #h1태그 (제목) 다가져옴. link도 같이 딸려온다

    for title_list in soup:
        try:
            href = title_list.a['href']     #링크 가져오기
            arr_url.append(href)
        except TypeError:
            print("err")

    print(arr_url)

    # return arr_url

url_crawling("http://techneedle.com/" , ("h1", {"class":"entry-title"}))
