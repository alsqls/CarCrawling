from urllib.request import Request, urlopen
import urllib.parse
from bs4 import BeautifulSoup

def Crawling():
    pages = 10;
    for page in range(len(pages)):
        html = Request('http://auto.danawa.com/newcar/?Work=search&Tab=&Brand=&Classify=&Fuel=&Tm=&Price=&Efficiency=&EfficiencyKind=&DriveWheel=&Displace=&ListType=list&Order=2&Punit=20&ListType=list&Page=' + str(page) , headers={'User-Agent':'Mozilla/6.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)'})
        webpage = urlopen(html).read()
        soup = BeautifulSoup(webpage , from_encoding="utf-8")
        carNum = soup.find_all("div" ,class_="num")
        print(len(carNum))
        car_title = soup.find_all("div" ,class_="title") # 배열
        print(car_title)



if __name__ == '__main__' :
    Crawling()
