cümle = str(input("Cümle Giriniz = "))

kelimeler = cümle.split()
kelimeler.sort()
print(kelimeler)
for kelime in cümle:
    print(kelime)