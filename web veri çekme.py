import requests
from bs4 import BeautifulSoup

imdburl = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
r = requests.get(imdburl)
soup = BeautifulSoup(r.content,"html parser")

gelenveri = soup.find_all("table",{"class":"chart full-width"})
print(gelenveri)