#%%
sehir = "Ankara"

print(sehir.upper())
print(sehir.endswith("e"))
#%%
def selamVer(isim = "dostum"):
    print("Merhaba " + isim)    
    
    
selamVer("Ömer")
selamVer()
#%%
def dikdörtgenAlan(kkenar,ukenar):     
    print(str(kkenar * ukenar))    
    
x=int(input("Kısa Kenar Giriniz = "))
y=int(input("Uzun Kenar Giriniz = "))

dikdörtgenAlan(x,y)
#%%
def dikucgenAlan(a,b):
    return a * b /2
a=int(input("Yükseklik = "))
b=int(input("Taban = "))
dikucgenAlan(a,b)
#%%
dikucgenAlanı2 = lambda c,d : c*d/2
print(dikucgenAlanı2(4,8))