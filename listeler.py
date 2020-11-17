sebzeler=["salata" , "domates" , "patlıcan" ,"salata"]
print(sebzeler[0])
print(sebzeler[:len(sebzeler)])
sebzeler.append(input("Sebze Giriniz = "))
print(sebzeler[:len(sebzeler)])
sebzeler.remove(input("Hangi Sebze Çıkartılsın = "))
print(sebzeler[:len(sebzeler)])
#print(sebzeler.clear()) # Listeyi Temizler
print("Salata Sayısı = "+ str(sebzeler.count("salata")))
print("Salatanın İndexi = " + str(sebzeler.index("salata"))) #İlk Bulduğunda Bitiriyor
print(sebzeler.pop(1))
print(sebzeler.insert(0,"kabak")) #İndex 0 a kabak yerleştir
print(sebzeler.reverse())
#sebzeler2 = sebzeler.copy # yedek almak
#sebzeler2[1]= "pırasa"
#print(sebzeler.extend(sebzeler2)) #Dizileri Birleştirir

sebzeler.sort() #Alfabetik sıralama
