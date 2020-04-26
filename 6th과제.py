import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

path = os.getcwd() +"/6th/chromedriver"

driver = webdriver.Chrome(path)

try :
    driver.get("https://www.cdc.go.kr/board/board.es?mid=a20504000000&bid=0014")
    time.sleep(1)

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    pages = bs.find("div", class_ ="board_pager").find_all("a")[-1]["href"].split("page")[1]
    pages = int(pages)

    title = []
    for i in range(3) :
        driver.get("https://www.cdc.go.kr/board/board.es?mid=a20504000000&bid=0014") + str(i + 1)
        time.sleep(3)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find_all("li", class_ = "title")
        title.append("page" + str(i+1))
        for c in conts :
            title.append(c.find("a").text)


finally :
    for t in title :
        if t.find("page") != -1 :
            print()
            print(t)
        else :
            print(t)
    time.sleep(3)
    driver.quit()