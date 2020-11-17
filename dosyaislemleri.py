#"r" okuma
#"a" data ekleyecem 
#"w" yoksa olutur bulunuyorsa ekleyecem
#"x" olutur bulunuyorsa hata alırsın

f = open("asalsayımı.py","r")

print(f.read()) #herseyi okur
print(f.read(15)) #15 karakter okur
print(f.readline()) #Satır Oku
for l in f:
    print(f.readline()) #Satır Oku
    
f.close()
    
#%%

dosyaekle = open("deneme.py","w")
dosyaekle.write("Omer" + "\n")
dosyaekle.write("Omer" + "\n")
dosyaekle.write("Omer" + "\n")
dosyaekle.write("Omer" + "\n")
dosyaekle.close()
#%%
import os

if os.path.exists("deneme.py"):
    os.remove("deneme.py")
    print("Dosya Bulunuyor")
else:
    print("Dosya Yok")
#%%
    
os.rmdir("klasor") #klasör silme
#%%
ogrenciler = ["Ömer","Faruk","Nihat","Mehmet","Zeynep"]

x = open("öğrenciler","a")

for ogrenci in ogrenciler:
    x.write(ogrenci)
    x.write("\n")
    

x = open("öğrenciler","r")
print(x.read())

x.close()