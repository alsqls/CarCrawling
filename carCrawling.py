from urllib.request import Request, urlopen
import urllib.parse
from bs4 import BeautifulSoup
#-*- coding:utf-8 -*-
def Crawling():
    titles = [] # 차 이름
    fuel_num = [] # 차 연비
    price_num = [] # 차 가격

    for page in range(1,15):
        html = Request('http://auto.danawa.com/newcar/?Work=search&Tab=&Brand=&Classify=&Fuel=&Tm=&Price=&Efficiency=&EfficiencyKind=&DriveWheel=&Displace=&ListType=list&Order=2&Punit=20&ListType=list&Page=' + str(page) , headers={'User-Agent':'Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)'})
        webpage = urlopen(html).read()
        soup = BeautifulSoup(webpage , from_encoding="utf-8")

        tmp = soup.find("ul" ,class_="modelList listType")
        car_title = tmp.find_all("div" ,class_="title")
        for i in car_title:
            titles.append(i.text)
        titles = [re.replace("\n","") for re in titles]
        print(len(titles))
        print(titles)

        car_fuel = soup.find_all("div" , class_="spec info")
        print(len(car_fuel)) #20

        for f in car_fuel :
            fuel = f.find("span", class_="num").text.strip()
            if '~' in fuel:
                fuel = fuel[fuel.index('~')+1:]
                fuel = fuel[:fuel.index(' ')]
            elif '미정' in fuel:
                fuel = "NA"
            else :
                fuel = fuel[:fuel.index(' ')]

            fuel_num.append(fuel)
        print(fuel_num)

        car_price = soup.find_all("div" ,class_="price")
        for f in car_price :
            price = f.find("span", class_="num").text.strip()
            if '~' in price:
                price = price[price.index('~')+2:]
            elif '미정' in price:
                price = "NA"
            else :
                price = price
            price = price.replace(',','')
            price_num.append(price)
        print(price_num)

if __name__ == '__main__' :
    Crawling()
