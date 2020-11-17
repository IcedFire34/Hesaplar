import requests
from bs4 import BeautifulSoup

print("""
Bu script hedef sistem hakkında bilgi toplamak için tasarlanmıştır.
by Iced Fire
""")
hedef = (input("Hedef : "))
dosya = open(hedef +" Hakkında Gerekli Bilgiler.txt","w+")
def Robtex(hedef):
    #Robtex ile veri toplama
    try:
        r = requests.get("https://www.robtex.com/dns-lookup/"+hedef)
        if (r.status_code == 200):
            print("Bağlantı Başarılı ...")
            soup = BeautifulSoup(r.content, "html.parser")
            GelenVeri = soup.find_all("div", {"class": "brx"})
            dosya.write("Robtex test sonuçları :" + "\n" + "\n")
            for item in GelenVeri:
                item = item.contents
                başlık = item[0].text
                içerik = item[1].find_all("li")
                dosya.write(başlık.upper() + "\n")
                dosya.write("---------------" + "\n")
                for iç in içerik:
                    dosya.write(iç.text + "\n")
                dosya.write("---------------" + "\n")
        elif (r.status_code == 502):
            print("Sunucuya Bağlanılamadı ! (Robtex)")
    except:
        print("Bağlantı ile ilgili hata oluştu tekrar deneyiniz (Robtex)")


Robtex(hedef)
dosya.close()