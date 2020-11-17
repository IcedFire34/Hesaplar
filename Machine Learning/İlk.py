# -*- coding: utf-8 -*-
#Gerekli Kütüphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Veri yükleme
veriler = pd.read_csv("veriler.csv")


#Veri ön işleme
   
boy = veriler[["boy","kilo"]]
print(boy)

#Eksik Veriler

eksikveriler = pd.read_csv("eksikveriler.csv")

from sklearn.impute import SimpleImputer as SI

imputer = SI(np.nan , strategy="mean")

yaş = eksikveriler.iloc[:,1:4].values
imputer = imputer.fit(yaş[:,1:4]) #Öğrenme
yaş[:,1:4] = imputer.transform(yaş[:,1:4]) #Uygulama

print(yaş)

#Kategorik veriler   
 
ülke = eksikveriler.iloc[:,0:1].values

from sklearn import preprocessing

le = preprocessing.LabelEncoder()
ülke[:,0] = le.fit_transform(eksikveriler.iloc[:,0])

print(ülke)

ohe = preprocessing.OneHotEncoder()
ülke = ohe.fit_transform(ülke).toarray()
print(ülke)