from urllib.request import Request, urlopen
import urllib.parse
from bs4 import BeautifulSoup

def Crawling():
    titles = []
    fuel_num = []
    price_num = []
    for page in range(1,15):
        html = Request('http://auto.danawa.com/newcar/?Work=search&Tab=&Brand=&Classify=&Fuel=&Tm=&Price=&Efficiency=&EfficiencyKind=&DriveWheel=&Displace=&ListType=list&Order=2&Punit=20&ListType=list&Page=' + str(page) , headers={'User-Agent':'Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)'})
        webpage = urlopen(html).read()
        soup = BeautifulSoup(webpage , from_encoding="utf-8")

        car_title = soup.find_all("div" ,class_="title") # 배열
        for i in car_title:
            titles.append(i.text)
        titles = [re.replace("\n","") for re in titles]
        #print(titles)

        car_fuel = soup.find_all("div" , class_="spec info")
        print(len(car_fuel)) #20
        for f in car_fuel :
            fuel_num.append(f.find_all("span", class_="num").contents[f])
        print(fuel_num)

        car_price = soup.find_all("div" ,class_="price")
        for f in car_price :
            price_num.append(f.find_all("span", class_="num"))
        print(price_num)

# text = '키워드'
#<span class="num">10.8~13.0 ㎞/ℓ</span>


if __name__ == '__main__' :
    Crawling()
