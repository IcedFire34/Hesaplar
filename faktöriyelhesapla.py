sayı = int(input("Sayı Giriniz = "))
carpım = 1
if sayı <0 :
    print("Negatif Sayıların Faktöriyeli Yoktur")
else:
    for x in range(1,sayı + 1):
        carpım = carpım * x   
    print(str(sayı) + " Faktöriyel = " + str(carpım))
