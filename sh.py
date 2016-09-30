# -*- coding: utf-8 -*-


import mechanicalsoup
from bs4 import BeautifulSoup

INTERNET_AND_SNS = 1
IT_TODAY = 2
IT_VIEW_POINT = 3
TECH_NEEDLE = 4

browser = mechanicalsoup.Browser()

# def url_crawling(argUrl,argForm):
#     # global arr_url
#     arr_url = list()
#
#     source = browser.get(argUrl)
#     soup = source.soup.findAll("h1", {"class":"entry-title"})     #h1태그 (제목) 다가져옴. link도 같이 딸려온다
#     for title_list in soup:
#         global arr_url
#         try:
#             href = title_list.a['href']     #링크 가져오기
#             arr_url.append(href)
#         except TypeError as e:
#             print("++++++++++++++++++++++++++++++++++")
#             print(e)
#
#
#     return arr_url
#
# ap = list()
# ap = url_crawling("http://techneedle.com/" , ("h1", {"class":"entry-title"}))
# print(ap[0])
# print(ap[1])

# 이중포문을 이용해 게시물 타이틀과 url주소, 컨텐츠를 뽑아냄



def url_crawling(argSiteNum, argUrl, argForm):
    arr_dict = list()    # 뽑아낸 정보들을 담을 리스트
    source = browser.get(argUrl)

    # soup = source.soup.findAll("td",{"class":"ArtList_Title") # 아이티투데이
    soup = source.soup.select(argForm) # 아이티투데이
    # soup = source.soup.select("ul > li > dl") # 네이버뉴스
    # print(soup)

    for websoup in soup:
        contents_info = dict()
        new_url  = "default"
        new_title = "default"
        new_content = "default"


        if argSiteNum == INTERNET_AND_SNS :
            try:
                if  websoup.dt['class'] is not None :
                    new_url = websoup.dt.a['href']
                    new_title = websoup.dt.img["alt"]
            except KeyError as e :
                new_url = websoup.dt.a['href']
                new_title = websoup.dt.a.text

            contents_info['url'] = new_url
            contents_info['title'] = new_title
            arr_dict.append(contents_info)

            source2 = browser.get(new_url)
            soup2 = source2.soup.select("div[id=articleBodyContents]")
            print(soup2)
            for websoup2 in soup2:
                new_content = websoup2.text
            contents_info['content'] = new_content
            arr_dict.append(contents_info)

        elif argSiteNum == IT_TODAY :
            new_url = websoup.a["href"]
            new_title = websoup.a.text
            contents_info['url'] = new_url
            contents_info['title'] = new_title

            new_url2 = argUrl[:30]+new_url
            # 게시물에 직접 들어가기 위해 필요한 소스 가공
            source2 = browser.get(new_url2)
            soup2 = source2.soup.select("td[class=view_r]")
            for websoup2 in soup2:
                new_content = websoup2.p.text
                # 왜 안 덮어 씌우지?? 왜지??? 왜 때문이지???
            contents_info['content'] = new_content
            arr_dict.append(contents_info)

        elif argSiteNum == IT_VIEW_POINT :
            new_url = ""
            new_title = ""

        elif argSiteNum == TECH_NEEDLE :
            new_url = ""
            new_title = ""

        print("정보:: ============== >>> ", contents_info)

    # return arr_dict()


# result =
# url_crawling(2, "http://www.ittoday.co.kr/news/articleList.html?sc_section_code=S1N11&amp;view_type=sm", ("td[class=ArtList_Title]") )
url_crawling(1, "http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=226", "ul > li > dl" )
# url_crawling(4, "http://techneedle.com/", )
