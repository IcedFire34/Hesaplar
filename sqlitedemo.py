import sqlite3

baglantı = sqlite3.connect("chinook.db")

sorgu = baglantı.execute ("select * from customers where city='Prague' or city='Berlin'")

for satır in sorgu :
    print("Adı : " + satır[1])
    print("SoyAdı : " + satır[2])
    print("***********")
    
    
baglantı.close()