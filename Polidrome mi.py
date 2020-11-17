#Girilen Sayının Polidrome olup olmadığını sorgulayan bir script (Polidrome : Normal okunuşu ve ters okunuşu aynı olan sayı demek)

def sorgula():
    sayı = input("Lütfen sorgulamak istediğiniz sayıyı giriniz : ")
    if sayı==sayı[::-1]:
        print(sayı + " Sayısı polidrom bir sayıdır")
    else:
        print(sayı + " Sayısı polidrom değildir")
sorgula()