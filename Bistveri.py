# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup



url = requests.get("https://www.borsaistanbul.com/veriler")
soup = BeautifulSoup(url.content,"html.parser")

print("""
Neler Yapmak İstiyorsunuz : 
1)Artanları Gör

""")

def artanlar():

    artanlar = soup.find_all("div" , {"class":"InvestorBottomContainer"})
    artanlartablosu = artanlar[0]
    artanlartablosu2 = artanlartablosu.find_all("tbody")

    for şirket in artanlartablosu2:
        isim = şirket.find_all("td",{"class":"left"})
        adet = len(isim)
        i=0
        print("Artanlar : \n")
        while i<=int(adet)-1: 
            isim = isim[i].text
            print(isim)
            i = i+1
            isim = şirket.find_all("td",{"class":"left"})       
            
artanlar()

