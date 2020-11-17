import sqlite3

con = sqlite3.connect("data.db")

cursor = con.cursor() 
#%% Database Fonksiyonları
def tabloolustur():    
    cursor.execute("CREATE TABLE IF NOT EXISTS kullanıcı (ad TEXT,soyad TEXT,eposta TEXT,dogumgunu TEXT,nick TEXT,pw TEXT)")

def degerekle():
    ad = str(input("Adınız Nedir : "))
    soyad = str(input("Soyadınız Nedir : "))
    eposta = str(input("E Posta Adresiniz Nedir : "))
    dogumgunu = str(input("Doğum Gününüz Nedir(GG.AA.YYYY) : "))
    nick = str(input("Kullanıcı Adınızı Giriniz : "))
    pw = str(input("Şifrenizi Giriniz : "))

    cursor.execute("INSERT INTO kullanıcı VALUES(?,?,?,?,?,?)",(ad,soyad,eposta,dogumgunu,nick,pw))
    
def degeral():
    cursor.execute("SELECT * FROM kulla
                   nıcı")
    global data
    data = cursor.fetchall()   
#%% Matematisel Fonksiyonlar
def asalmı():
    sayı = int(input("Sayı Giriniz = "))
    asalmı = "evet"
    for x in range(2,sayı):
        if sayı % x == 0:
            asalmı = "hayır"
            print()
            break    
        if asalmı == "evet":
            print("Asal")
        else:
            print("Asal Değil")
            
class Matematik:
    def topla(self,x,y):
        return(x + y)
    def cıkar(self,x,y):
        return(x - y)
    def carp(self,x,y):
        return(x * y)
    def bol(self,x,y):
        return(x / y)

matematik = Matematik()
  
#%%  
    

#%% Kullanıcı Bilgileri Kontrol    
tabloolustur()
degeral()

if data == [] :    
    print("Lütfen İlk Önce Kendinizi Tanıtın")
    degerekle()
#%%
# Kullanıcı Verileri
print(data)
ad = data[0][0]      
soyad =  data[0][1]   
eposta = data[0][2]   
dg = data[0][3]
nick = data[0][4]
pw = data[0][5]
#%%
con.commit()
con.close()
#%%

print("""
      -------------------------
      -                       -
      -                       -
      -  MERHABA HOŞGELDİNİZ  -
      -                       -
      -                       -
      -------------------------
      """)
i = 0
while i == 0:
    emir = str(input("Nasıl Yardımcı Olabilirim ? "))
    emir.lower()
    if emir == "beyn":
        print("Buyrun " + str(ad))
    elif emir == "f" :
        i = 1