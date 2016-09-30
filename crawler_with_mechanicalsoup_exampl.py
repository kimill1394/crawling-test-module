# -*- coding = utf-8 -*-

import mechanicalsoup

browser= mechanicalsoup.Browser()
source = browser.get("http://techneedle.com/")
# browser.get의 반환값은 self.session.get = response
# add_soup()를 실행시킴, 이 과정에서 response를 생성하고 반환!
# response를 생성하면서 soup=bs4() 생성!!
soup = source.soup.findAll("h1", {"class":"entry-title"})     #h1태그 (제목) 다가져옴. link도 같이 딸려온다
# print('===',source.text)

#   print(type(soup))
#   soup의 반환형은 bs4.element.resultset 객체이다.
#   객체의 요소에 .으로 접근 가능하다.

global arrlist
arrlist=list()


for title_list in soup:
    arrlist.append(title_list.a['href'])     #링크 가져오기


print(arrlist," title :")
