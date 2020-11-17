import random
class dusman:   
    def __init__(self,isim = "Düşman",can = 10,güc = 20,mermi=39):
        
        self.isim = isim
        self.can= can
        self.güc = güc
        self.mermi = mermi    
    
    def print(self):
        print("Yükleniyor ...")
        print("İsim : " , self.isim , " Kalan can : " , self.can , " Güç : " , self.güc," Mermi : " , self.mermi)
     
    def saldır(self):
        print(self.isim + " Saldırıyor")
        harcanan_mermi = random.randrange(1,10)
        print(str(harcanan_mermi) + " Mermi Harcandı")
        self.mermi = self.mermi-harcanan_mermi
        
        return (harcanan_mermi,self.güc)
    
    def hasar_ye(self,harcanan_mermi,saldırı_gücü):
        print(self.isim + " Vuruldum ...")
        self.can = self.can - (harcanan_mermi * saldırı_gücü)
        print(self.isim + " Can: " + str(self.can))       
        
    def mermi_kntrl(self):
        if self.mermi <=0:
            print(self.isim + " Konuşuyor : ""Mermi Bitti ...")
            return True
        else:
            return False
    def hayatt_mı(self):
        if self.can <=0:
            print("ÖLdüm ...")
        else :
            print("Hayattayımmmm")
            
    
dusmanlar = []

i = 0

while i<10:
    rastgele_can = random.randrange(0,10)
    rastgele_güc = random.randrange(1,2)
    rastgele_mermi = random.randrange(0,5)
    yenidüşman = dusman("Düşman " + str(i+1),rastgele_can,rastgele_güc,rastgele_mermi)
    dusmanlar.append(yenidüşman)
    i+=1
    
i = 0

while i <3:
    randomdusman1 = random.randrange(0,9)
    randomdusman2 = random.randrange(0,9)
    
    dönendeger = dusmanlar[randomdusman1].saldır()
    dusmanlar[randomdusman2].hasar_ye(dönendeger[0],dönendeger[1])
    dusmanlar[randomdusman2].hayatt_mı()
    
    print("Raund Bitti ... \n")
    i+=1
    
#%% Kalıtım 
    
class Çalışan():
    
    def __init__(self,isim,maaş,departman):
        print("Çalışan Sınııfının Yapıcı Fonksiyonları")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
        
    def bilgilerigöster(self):
        print("Çalışan Sınıfının Bilgileri Gösteriliyor ...")
        print("İsim : " , self.isim , " Maaş : " , self.maaş , " Departman : ",self.departman)
    def zam(self,miktar):
        print("Maaşa Zam Yapıldı")
        self.maaş = self.maaş + miktar
    def depertmandegiştir(self,yenidepertman):
        print("Depertman Değiştiriliyor ...")
        self.Depertman = yenidepertman
        
class Yönetici(Çalışan):
    def __init__(self,isim,maaş,depertman ,kişisayısı):
        print("Yönetici Sınıfının Yapıcı Fonksiyonları")
        super().__init__(isim,maaş,depertman)
        self.kişisayısı = kişisayısı
        
    def bilgilerigöster(self):
        print("Yönetici Sınıfının Bilgileri Gösteriliyor ...")
        print("İsim : " , self.isim , " Maaş : " , self.maaş , " Departman : ",self.departman ," Personel Sayısı : ",self.kişisayısı)    
      
    def işçial(self,kişi):
        print("Kişi Sayısı Arttırılıyor ...")
        self.kişisayısı += kişi        


yönetici = Yönetici("Boss",1000000,"Patron",45)
yönetici.işçial(23)
yönetici.bilgilerigöster()
#%%

    
class öğrenci():
    def dersçalış(self):
        print("Ders Çalışıyor")
    
class çalışan():
    def çalış(self):
        print("Personel Çalışıyor")

class Yazılımcı(öğrenci,çalışan):
    pass

yazılımcı = Yazılımcı()
yazılımcı.dersçalış()
yazılımcı.çalış()
#%%





