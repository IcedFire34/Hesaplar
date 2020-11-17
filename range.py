#%%
for x in range(50,100,2):
    print(x)
    
#%%

sayı=int(input("Kaç Yıldız = "))
yıldız = ""

for x in range(1,sayı + 1):
    yıldız = yıldız + "*"
    print(yıldız)
    
#%%
i = 0
kelime = ""
while i<=10:  
    if kelime == "":
        print(kelime + "ö")
        kelime = "ö"
    elif kelime == "ö":
        print(kelime + "m")
        kelime = "öm"
    elif kelime == "öm":
        print(kelime + "e")
        kelime = "öme"
    elif kelime == "öme":
        print(kelime + "r")
        kelime = "ömer"
    elif kelime == "ömer":
        print("ö")
        kelime = "ö"
    i = i + 1
    
    