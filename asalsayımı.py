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