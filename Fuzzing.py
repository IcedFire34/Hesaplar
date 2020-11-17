import requests
dosya = open("Fuzzing.txt","r")
içerik = dosya.read()
dosya.close()
hedef = str(input("Hedef Site : "))
for i in içerik.split("\n"):
    try:
        url = hedef + str(i)
        req = requests.get(url)
        if (req.status_code == 200):
            print(url)
        else:
            print("Bağlantı Başarısız " + url)
    except:
        pass
