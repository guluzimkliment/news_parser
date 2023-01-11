# Default modules - Модули по умолчанию
import csv
import time
import json
import random
import datetime
from os import system

# Downloaded libraries - Скаченные библиотеки
import requests
from bs4 import BeautifulSoup

# Created module - Созданный модуль
from core.config import DOMEN, URL, HEADERS

# сделали headers по умолчанию можно не передавать ее при  вызове функции
def get_responce(url_def,headers_def= HEADERS): # отправляем запрос 
    response = requests.get(url=url_def,headers=headers_def)
    #
    if response.status_code == 200:
        src= response.content
        return src
    else:
        print(f"что то пошло не по плану {response.ststus_code}")
news_info =[]
def get_soup(response):
    soup = BeautifulSoup(response , 'lxml')
    all_news = soup.find_all("div", class_="tn-news-author-list-item")
    
    for item  in all_news:
        try:
            title = item.find("div",class_="tn-news-author-list-item-text").find("span", class_="tn-news-author-list-title")
            description = item.find("div", class_="tn-news-author-list-item-text").find("p", class_="tn-announce")
            date_time = item.find("div", class_="tn-news-author-list-item-text").find("li")
            news_url = DOMEN + item.find("a").get("href")
            image = item.find("div", class_="tn-image-container").find("img").get("src")
        except:
            image = item.find("div", class_="tn-video-container").find("source").get("src")
            information = {
            "title": title.text,
            "description": description.text,
            "date_time": date_time.text.strip(),
            "image": DOMEN + image,
            "url": news_url
        }
        else:
            information = {
            "title": title.text,
            "description": description.text,
            "date_time": date_time.text.strip(),
            "image": DOMEN + image,
            "url": news_url
        }
    news_info.append(information)
    return news_info

def parser():
    response = get_responce(url_def=URL)
    soup = get_soup(response)

    with open(f"core/json/tengrinews.json", "w", encoding="UTF-8") as file:
        json.dump(soup, file, ensure_ascii=False, indent=4)#ensure ascii - чтобы и русские буквы читал 
    
parser()

# response = requests.get(url=URL, headers=HEADERS)
# src = response.text
# with open("core/html/index.html", "w") as file:
#     file.write(src)
# with open("core/html/index.html", "r") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "html.parser")

# news = soup.find_all("div", class_="tn-news-author-list-item")
# teg_image = soup.find_all("div", class_="tn-image-container")

# news_info = []
# for item in news:
#     try:
#         title = item.find("div", class_="tn-news-author-list-item-text").find("span", class_="tn-news-author-list-title")
#         description = item.find("div", class_="tn-news-author-list-item-text").find("p", class_="tn-announce")
#         date_time = item.find("div", class_="tn-news-author-list-item-text").find("li")
#         news_url = DOMEN + item.find("a").get("href")
#         image = item.find("div", class_="tn-image-container").find("img").get("src")
#     except:
#         image = item.find("div", class_="tn-video-container").find("source").get("src")
#         information = {
#         "title": title.text,
#         "description": description.text,
#         "date_time": date_time.text.strip(),
#         "image": DOMEN + image,
#         "url": news_url
#     }
#     else:
#         information = {
#         "title": title.text,
#         "description": description.text,
#         "date_time": date_time.text.strip(),
#         "image": DOMEN + image,
#         "url": news_url
#     }
    
#     news_info.append(information)

# with open(f"core/json/tengrinews.json", "w", encoding="utf-8") as file:
#     json.dump(news_info, file, indent=4, ensure_ascii=False)