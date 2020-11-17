#YORUM SATIRI
mesaj = "Selamun Aleyküm"

print(mesaj[0:7])

yenimesaj = mesaj[ 0:7]
print(yenimesaj)
print(mesaj[:5])
print(len(mesaj)) #Metin Uzunluğunu Bulmaya Yarar
print(mesaj[len(mesaj)-1:len(mesaj)])

#Lower - Upper

print(mesaj.upper())
print(mesaj.lower())

print(mesaj.replace("e","a"))

print(mesaj.replace("Selamun Aleyküm","Aleyküm Selam"))

print(mesaj.split()) #Kelimeleri Böler
print(mesaj.strip()) #Bastaki ile sondaki boslukları kaldırır
print("Aleyküm = " + mesaj.split()[1])

#input

ad= input("Adınız ?")
print(ad)

#dikdörtgen alan hesabı
ukenar=input("Uzun Kenar ?")
kkenar=input("Kısa Kenar ?")
alan = int(ukenar) * int(kkenar)
print("Alan = " + str(alan) )

#WorkShops
#Değişken Değiştirme
x=10
y=20

x,y = y,x

gecici = x
x=y 
y=gecici

print("x = " + str(x) , "y = " + str(gecici))

#Kaç Mil Eder
milkackm = 1,609344

km = int(input("Kaç Km = "))

mil = km / 1,609344
print("Mil = " + str(mil))