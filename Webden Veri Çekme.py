import requests
from bs4 import BeautifulSoup as bs

imdburl = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
r = requests.get(imdburl)
soup = bs(r.content,"html.parser")
gelenveri = soup.find_all("table",{"class":"chart full-width"})
#print(gelenveri[0].contents)
filmtablosu = (gelenveri[0].contents)[len(gelenveri[0].contents) -2 ]
filmtablosu = filmtablosu.find_all("tr")

for film in filmtablosu:
    filmbaslıkları = film.find_all("td",{"class" : "titleColumn"})
    filmismi = filmbaslıkları[0].text
    filmismi = filmismi.replace("\n","")
    print(filmismi)
    print("***********************************")