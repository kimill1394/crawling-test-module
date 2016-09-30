# -*- coding: utf-8 -*-


import mechanicalsoup
from bs4 import BeautifulSoup

browser= mechanicalsoup.Browser()

def url_crawling(argUrl):
    arr_url = list()
    arr_title = list()

    source = browser.get(argUrl)
    # soup = source.soup.findAll(argForm)     #h1태그 (제목) 다가져옴. link도 같이 딸려온다
    soup = source.soup.select("ul > li > dl");
    # print("aaaaaaaaaaaaaaaaaaaaaaaa=====soup: ", soup)

    for title_list in soup:
        try:
            if title_list.dt['class'] is not None : # dt 첫번째에 이미지가 있는 경우 두 번째 태그에서 가져와야 함
                href = title_list.dt.a['href']     #링크 가져오기
                arr_url.append(href)
                title = (title_list.dt.img["alt"])
                arr_title.append(title)
        except TypeError:
            print("err")
        except KeyError:        # 비교식에서 예외 발생, class가 없는 경우
            href = title_list.dt.a['href']     #링크 가져오기
            arr_url.append(href)
            title = title_list.dt.a.text
            arr_title.append(title)
        finally :
            print("href: ", href)
            print("title: ", title)
            print(" ")
            print(" ")
            # print(title_list.a.text)


    print(arr_url)


    # return arr_url

url_crawling("http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=732")
