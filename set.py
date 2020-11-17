isimler = {"ali","ahmet","ömer","faruk"}
#sayılar = set(5,7,9,25,53,858,512,45)
print(isimler)

for marul in isimler:
    print(marul)
    
print("ali" in isimler)

if "ali" in isimler:
    print("listede bulunuyor")

if 1 <2 :
    print("2 birden büyük")
    
isimler.add("eslem")
print(isimler)
isimler.update(["Kerem","Mahmut","Yağmur"])
print(isimler)
isimler.discard("ali")
print(isimler)
#isimler.clear()

setA={1,5,4,6}
setB={2,5,9,7}
print(setA | setB) #setleri birleştirme
print(setA & setB) #ortakları gösterir
print(setA - setB) #setA nın setB den farkı
print(setA ^ setB) #Kesişimler Hariçler
