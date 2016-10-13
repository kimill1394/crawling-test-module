# -*- coding: utf-8 -*-

import sys
import mechanicalsoup
from bs4 import BeautifulSoup

# 직관적 if문을 위한 리터럴 상수(처럼 쓰고 싶은 변수 ㅎㅎ)
# 매개변수를 int형으로 받을 수가 없어서 문자열로 선언함.
INTERNET_AND_SNS = "1"
IT_TODAY = "2"
IT_VIEW_POINT = "3"
TECH_NEEDLE = "4"

#함수에서 사용할 browser객체, 아무래도 좋으니까 함수 밖에 선언
browser = mechanicalsoup.Browser()

def url_crawling(argSiteNum, argUrl, argForm):
    arr_dict = list()
    # 뽑아낸 정보들을 담을 리스트(안에는 딕셔너리를 넣습니다!)
    source = browser.get(argUrl)
    soup = source.soup.select(argForm)


    for websoup in soup:
        contents_info = dict()
        # 한 게시물 당 정보를 담을 딕셔너리! 값은 아래 세가지!
        new_url  = "default"
        new_title = "default"
        new_content = "default"


        if argSiteNum == INTERNET_AND_SNS :
            # 네이버 IT 뉴스 == 1
            try:
                if  websoup.dt['class'] is not None :
                    # 처음에 이미지가 존재하지 않으면 해당 비교식에 들어가기 전에 websoup.dt['class']를 가져오는 것 부터 에러가 발생, 아래 KeyError에서 이를 처리합니다욥
                    # 즉! 이미지가 존재하고 그 값이 None이 아닌 경우!
                    # 참고로, 이미지가 존재하면 dt / dt / dd 의 구조를 이루고 이미지가 존재하지 않으면 dt/ dd 의 구조를 이루고 있어 내용이 다르기 때문에 ㅎㅎ
                    new_url = websoup.dt.a['href']
                    new_title = websoup.dt.img["alt"]
            except KeyError as e :
                # python에서의 예외처리 문장
                new_url = websoup.dt.a['href']
                new_title = websoup.dt.a.text

            # url과 title을 다 뽑았으니 이제 딕셔너리에 등록하고
            contents_info['url'] = new_url
            contents_info['title'] = new_title
            # 딕셔너리에 등록한 정보 전부를 리스트에 넣습니당
            arr_dict.append(contents_info)

            # 각 게시물의 컨텐츠를 뽑기 위해 게시물 하나하나 직접 접근!
            source2 = browser.get(new_url)
            soup2 = source2.soup.select("div[id=articleBodyContents]")


            for websoup2 in soup2:
                new_content = websoup2
            contents_info['content'] = new_content
            arr_dict.append(contents_info)

        elif argSiteNum == IT_TODAY :

            new_url = websoup.a["href"]
            # new_url = websoup.select("div[class=se_post_function]")
            new_title = websoup.a.text
            contents_info['url'] = new_url
            contents_info['title'] = new_title

            # ittoday는 특이하게 a태그에서 긁어온 값만으로는 접근할 수 없음!
            # 따라서 직접 url을 가공해야 합니다 아래와 같이!
            new_url2 = argUrl[:30]+new_url
            source2 = browser.get(new_url2)
            soup2 = source2.soup.select("td[class=view_r]")


            for websoup2 in soup2:
                new_content = websoup2.p
            contents_info['content'] = new_content
            arr_dict.append(contents_info)

        # 5페이지 한꺼번에 보는 블로그였기 때문에 방식이 약간 다름
        elif argSiteNum == IT_VIEW_POINT :
            # url복사에서 직접 지정된 url(속성명 title)을 따야 함
            # select로 선택된 객체가 리스트이며 저장된 정보가 태그를 포함하고 있기 때문에 태그를 제외한 주소값을 얻기 위해 내용물이 하나뿐인 soup2를 순회해 주소를 얻는다
            soup2 = websoup.select("div[class=se_post_function]")
            for websoup2 in soup2:
                new_url = websoup2.a['title']

            new_title = websoup.h3.text
            # 한 페이지에 모든 게시물이 있었기 때문! 위의 url 추출과정과 비슷하지만 태그를 생략할 필요가 없으므로 배열 자체에 접근했슴니다
            # 불필요한 태그가 많이 딸려올 경우 순회로 수정하면 됨니다 말해주세욥
            new_content = websoup.select("div[class='se_component_wrap sect_dsc __se_component_area']")[0]
            # soup3 = websoup.select("div[class='se_component_wrap sect_dsc __se_component_area']")
            # for websoup3 in soup3 :
            #     new_content = websoup3
            contents_info['url'] = new_url
            contents_info['title'] = new_title
            contents_info['content'] = new_content
            arr_dict.append(contents_info)

        elif argSiteNum == TECH_NEEDLE :
            new_url = websoup.a['href']
            new_title = websoup.a.text
            contents_info['url'] = new_url
            contents_info['title'] = new_title

            source2 = browser.get(new_url)
            soup2 = source2.soup.select("div[class=insight_block_description]")
            for websoup2 in soup2:
                new_content = websoup2
            contents_info['content'] = new_content
            arr_dict.append(contents_info)

    # return arr_dict



    print(arr_dict);



# 함수를 실행하는 부분!
# url_crawling("2", "http://www.ittoday.co.kr/news/articleList.html?sc_section_code=S1N11&amp;view_type=sm", "td[class=ArtList_Title]" )
# url_crawling("1", "http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=226", "ul > li > dl" )
# url_crawling("4", "http://techneedle.com/", "h1[class=entry-title]")
url_crawling("3", "http://blog.naver.com/PostList.nhn?blogId=smashhit&from=postList&categoryNo=17", "div[class='se_doc_viewer se_body_wrap se_theme_transparent ']")





#매개변수 입력
# input_num = sys.argv[1]
# input_url = sys.argv[2]
# input_form = sys.argv[3]
#
#
# url_crawling(input_num,input_url,input_form)
