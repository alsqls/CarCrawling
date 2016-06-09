from urllib.request import Request, urlopen
import urllib.parse
from bs4 import BeautifulSoup

def Crawling():
    page = 1
    html = Request('http://auto.danawa.com/newcar/?Work=search&Tab=&Brand=&Classify=&Fuel=&Tm=&Price=&Efficiency=&EfficiencyKind=&DriveWheel=&Displace=&ListType=list&Order=2&Punit=20&ListType=list&Page=' + str(page), headers={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(html).read()
    soup = BeautifulSoup(webpage , from_encoding="utf-8")
    carNum = soup.find_all("div" ,class_="num")
    print(len(carNum))


if __name__ == '__main__' :
    Crawling()
