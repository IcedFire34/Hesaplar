sayı = int(input("Bir Sayı Giriniz ="))

if sayı>0:
    print("Sayı Pozitif")
elif sayı == 0:
    print("Sayı Sıfır")
elif sayı<0:
    print("Sayı Negatif")
    
sayı1 = int(input("1.Sayı :"))
sayı2 = int(input("2.Sayı :"))
sayı3 = int(input("3.Sayı :"))

if sayı1>sayı2 and sayı1>sayı3:
    print("En Büyük Sayı : " + str(sayı1))
elif sayı2>sayı1 and sayı2>sayı3:
    print("En Büyük Sayı : " + str(sayı2))
else:
    print("En Büyük Sayı :" + str(sayı3))