# -*- coding = utf-8 -*-

import requests # 웹 상의 데이터를 처리하기 위한 모듈
# import bs4.BeautifulSoup # 이거안됨
# import urllib.request # 이거됨
from bs4 import BeautifulSoup # HTML이나 XML코드를 가독성 좋게 가공하는 모듈

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://creativeworks.tistory.com/'+str(page)
        source_code = requests.get(url)
        # url에서 코드를 전부 요구(request), response 객체(source_code)를 만듦
        plain_text = source_code.text
        # text는 response 객체가 가지고 있는 값 중 하나로 유니코드로 되어있는 응답의 내용물 부분.

        soup = BeautifulSoup(plain_text, 'html.parser', from_encoding='utf-8')
        # BeautifulSoup객체를 만드는데 파라미터는 html문서
        # parser는 바꿀 수 있는데 아직 모르겟음 ㅠㅠ


        # for link in soup.select('h3 > a'):
            #  href = "http://creativeworks.tistory.com"+link.get('href')
            #  title = link.string
            #  print(href)
            #  print(title)
        # for title_list in soup.find_all(['h3','class']):
            # title = link.text
            # href = url
            # print(href)
            # print(title)

        for title_list in soup.find_all('div',{'class':'area_title'}):  # find_all  또는 findAll

            title = title_list.h3.text
            href = title_list.a['href']

            print(url,href)
            print(title)

        page+=1

spider(50)
