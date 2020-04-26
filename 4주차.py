import requests
from bs4 import BeautifulSoup
import csv

class BestScraper:

    def __init__(self):
        self.url = "http://www.11st.co.kr/html/bestSellerMain.html"


    def getHTML(self):
        res = requests.get(self.url)
        if res.status_code != 200:
            print("bad request", res.status_code)
        html = res.text
        soup = BeautifulSoup(html, "html.parser")
        return soup


    def getThings(self, soup):
        soup = self.getHTML()
        whole = soup.find_all("li", class_="viewtype catal_ty")

        name = []
        price = []

        for j in whole:
            if j.find("strong", class_="sale_price") != None:
                price.append(j.find("strong", class_="sale_price").text)
            if j.find("p", class_="pname") != None:
                name.append(j.find("p", class_="pname").text)

        self.writeCSV(name, price)

    def writeCSV(self, name, price):
        file = open("untitled.csv", "a", newline="", encoding='UTF8')
        wr = csv.writer(file)
        for i in range(len(name)):
            wr.writerow([name[i], price[i]])
        file.close

    def scrap(self):

        file = open("untitled.csv", "w", newline="", encoding='UTF8')
        wr = csv.writer(file)
        wr.writerow(["판매물품", "가격"])
        file.close()

        self.getContent(self)


if __name__ == "__main__":
    s = BestScraper()
    s.scrap()