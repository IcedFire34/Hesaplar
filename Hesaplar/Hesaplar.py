import sqlite3
baglan = sqlite3.connect("hesaplar.db")
imlec = baglan.cursor()

print("\033[92m" + """
      FONKSİYONLAR : 
      0)FONKSİYONLAR LİSTESİNİ ÇAĞIR
      1)HESAP BİLGİLERİ EKLE
      2)HESAP BİLGİLERİNİ GÖR
      3)HESAP BİLGİLERİNİ GÜNCELLE
      4)HESAP BİLGİLERİNİ SİL
      5)HESAP BİLGİLERİNİ YEDEKLE
      6)ÇIKIŞ YAP
""")

def tablo_olustur():
    imlec.execute("CREATE TABLE IF NOT EXISTS hesaplar (hesapadı TEXT,id TEXT,parola TEXT)")
    imlec.execute("CREATE TABLE IF NOT EXISTS sahip (isim TEXT ,şifre TEXT)")
    baglan.commit()  
    
def sahip_bilgileri():
    imlec.execute("SELECT isim FROM sahip")
    bilgi = imlec.fetchall()    
    if bilgi == [] :        
        isim = str(input("İsminiz : "))
        şifre = str(input("Şifre : "))
        imlec.execute("INSERT INTO sahip VALUES (?,?)",(isim,şifre))
        baglan.commit()
    else:
        imlec.execute("SELECT isim FROM sahip")
        isim = imlec.fetchall()
        isim = str(isim[0])        
        isim = isim.replace("(","").replace("'","").replace(")","").replace(",","")     
        print("Hoşgeldin : " + isim + "\n")
        girilenşifre = (input("Şifre : "))
        if girilenşifre != imlec.execute("SELECT soyisim FROM sahip"):
            print("Şifreyi YANLIŞ Girdiniz")
            baglan.close()
            exit()                    

def hesap_ekle():
    a=str(input("Hesap Nerede ? :"))
    b=str(input("E-mail ya da Kullanıcı Adıdını Giriniz :"))
    c=str(input("Parolayı Giriniz :"))
   
    imlec.execute("INSERT INTO hesaplar VALUES(?,?,?)" , (a,b,c)) 
    baglan.commit()
    print("Hesap Eklendi ... \n")   
    
def hesap_gör():
    print("Mevcut Hesaplar : \n")
    imlec.execute("SELECT * FROM hesaplar")
    veri = imlec.fetchall()
    for i in veri:
        print(i)
    print("\n")
        
def güncelle():
    hesap_upt = str(input("Hangi Hesabı Güncelleyeceksiniz : "))
    yeni_parola=str(input("Yeni Şifreyi Giriniz : "))    
    imlec.execute("UPDATE hesaplar SET parola=? WHERE id = ? ",(yeni_parola,hesap_upt))
    baglan.commit()
    print("Başarıyla Güncellendi ... \n")
        
def imha():
    imlec.execute("DELETE FROM hesaplar")
    baglan.commit()
    print("İMHA EDİLDİ ... \n")
        
def yedek():
    imlec.execute("SELECT * FROM hesaplar")
    yedek_veri = str(imlec.fetchall())
    dosya_olustur = open("yedek.txt","w")
    dosya_olustur.write(yedek_veri)
    print("Yedek Oluşturuldu ... \n")
    dosya_olustur.close()
    
def parolayıdegistir():
    imlec.execute("UPDATE sahip SET şifre=? WHERE id=?", ("","Ömer Faruk"))
    
tablo_olustur()
sahip_bilgileri()


talep=int(input("Ne Yapmak İstiyorsunuz(Numaraları Giriniz) :"))

while True:
    if talep == 1:
        hesap_ekle()
        talep=int(input("Ne Yapmak İstiyorsunuz(Numaraları Giriniz) :"))
    elif talep == 2:
        hesap_gör()
        talep=int(input("Ne Yapmak İstiyorsunuz(Numaraları Giriniz) :"))
    elif talep == 3:
        güncelle()
        talep=int(input("Ne Yapmak İstiyorsunuz(Numaraları Giriniz) :"))
    elif talep ==4:
        imha()
        talep=int(input("Ne Yapmak İstiyorsunuz(Numaraları Giriniz) :"))
    elif talep ==5:
        yedek()
        talep=int(input("Ne Yapmak İstiyorsunuz(Numaraları Giriniz) :"))
    elif talep ==6:
        baglan.close()
        print("Bağlantı Kesildi ... \n")
        break
    elif talep == 0:
        print("\033[92m" + """
          FONKSİYONLAR : 
          0)FONKSİYONLAR LİSTESİNİ ÇAĞIR
          1)HESAP BİLGİLERİ EKLE
          2)HESAP BİLGİLERİNİ GÖR
          3)HESAP BİLGİLERİNİ GÜNCELLE
          4)HESAP BİLGİLERİNİ SİL
          5)HESAP BİLGİLERİNİ YEDEKLE
          6)ÇIKIŞ YAP      
        """)
        talep=int(input("Ne Yapmak İstiyorsunuz(Numaraları Giriniz) :"))
    else :
        print("Hatalı Fonksiyon İstediniz ... \n")
        talep=int(input("Ne Yapmak İstiyorsunuz(Numaraları Giriniz) :"))