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
in1=int(input("Sayı1 = "))
in2=int(input("Sayı2 = "))

print(matematik.topla(in1,in2))  

#%%

class Person:
    def __init__(self,adı,soyadı,yas):
        self.adı = adı
        self.soyadı= soyadı
        self.yas = yas
x = str(input("Adınız = "))
y = str(input("SoyAdınız = "))
z = int(input("Yasınız = "))
person1 = Person(x,y,z)
print("Adınız = " + x + " SoyAdınız = " + y + " Yasınız = " + str(z))

#%%

class Çalısan(Person):
    def __init__(self,maas):
        self.maas = maas

class Müsteri(Person):
    def __init__(self,kredikartı):
        self.kredikartı = kredikartı
        
ahmet = Müsteri()

mehmet = Çalısan()
#%%
import matematikmodül

matematikmodül.carp(2,3)
#%%

import matematikmodül as mm

mm.carp(4,5)

#%%

from matematikmodül import topla

topla(8,15)

























        