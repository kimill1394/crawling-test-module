# -*- coding: utf-8 -*-

import sys
import mechanicalsoup
from bs4 import BeautifulSoup

import json #json import

INTERNET_AND_SNS = "1"
IT_TODAY = "2"
IT_VIEW_POINT = "3"
TECH_NEEDLE = "4"

browser = mechanicalsoup.Browser()

def url_crawling(argSiteNum, argUrl, argForm, argForm2):
    arr_dict = list()
    source = browser.get(argUrl)
    soup = source.soup.select(argForm)


    for websoup in soup:
        contents_info = dict()
        new_url  = "default"
        new_title = ""
        new_content = ""


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

        elif argSiteNum == IT_TODAY :
            new_url = websoup.a["href"]
            new_title = websoup.a.text
            contents_info['title'] = new_title
            new_url2 = argUrl[:30]+new_url
            contents_info['url'] = new_url2
            arr_dict.append(contents_info)


        elif argSiteNum == IT_VIEW_POINT :
            soup2 = websoup.select(argForm2)
            for websoup2 in soup2:
                new_url = websoup2.a['title']
            new_title = websoup.h3.text
            new_content = websoup.select("div[class='se_component_wrap sect_dsc __se_component_area']")[0]
            contents_info['url'] = new_url
            contents_info['title'] = new_title
            arr_dict.append(contents_info)

        elif argSiteNum == TECH_NEEDLE :
            new_url = websoup.a['href']
            new_title = websoup.a.text
            contents_info['url'] = new_url
            contents_info['title'] = new_title
            arr_dict.append(contents_info)

    print(json.dumps(arr_dict))

#매개변수 입력
input_num = sys.argv[1]
input_url = sys.argv[2]
input_major_form = sys.argv[3]
input_minor_form = sys.argv[4]


url_crawling(input_num , input_url , input_major_form , input_minor_form)
