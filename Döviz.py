import requests
from bs4 import BeautifulSoup
import time
import datetime

while True: 
    def altın_gör():
        altın = gramaltın.find_all("span",{"class":"value"})
        altın = altın[0].text
        print("Gram altın : " + altın + " tl")        
        
    def dolar_gör():
        deger = dolar.find_all("span",{"class":"value"})
        deger = deger[0].text
        print("Dolar : " + deger + " tl")
        deger=""
        
    def euro_gör():
        deger = euro.find_all("span",{"class":"value"})
        deger = deger[0].text
        print("Euro : " + deger + " tl")
        deger=""
        
    def sterlin_gör():
        deger = sterlin.find_all("span",{"class":"value"})
        deger = deger[0].text
        print("Sterlin : " + deger + " tl")
        deger=""
        
    def bist100_gör():
        deger = bist100.find_all("span",{"class":"value"})
        deger = deger[0].text
        print("Bist100 : " + deger)
        deger=""
        
    def faiz_gör():
        deger = faiz.find_all("span",{"class":"value"})
        deger = deger[0].text
        print("Faiz : " + deger)
        deger=""
        
            
        
url = "https://www.doviz.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
    
baner = soup.find_all("div",{"class":"market-data"})
baner2 = baner[0]
baner3 = baner2.find_all("a")

gramaltın = baner3[0]
dolar = baner3[1]
euro = baner3[2]
sterlin = baner3[3]
bist100 = baner3[4]
faiz = baner3[5]
deger = ""
            
tarih = datetime.datetime.now()
    
print("Şu Saat Ve Tarihteki Döviz Bilgileri : " + str(tarih) + "\n")
altın_gör()
dolar_gör()
euro_gör()
sterlin_gör()
bist100_gör()
faiz_gör()
url = ""
r = ""
soup = ""
baner = ""
baner2 = ""
baner3 = ""
time.sleep(10)
    
    
    