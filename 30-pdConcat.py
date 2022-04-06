import numpy as np
import pandas as pd
from pandas.core.reshape.concat import concat
sozluk1={"isim":["ahmet","mehmet","zeynep","atıl"],
        "spor":["koşu","yüzme","koşu","basketbol"],
        "kalori":[100,200,250,150]}
sozluk2={"isim":["akif","şerif","yusuf","furkan"],
        "spor":["koşu","yüzme","koşu","basketbol"],
        "kalori":[250,300,100,150]}
sozluk3={"isim":["samet","ömer","hüseyin","serkan"],
        "spor":["koşu","yüzme","badminton","tenis"],
        "kalori":[100,300,750,150]}
dataFrame1=pd.DataFrame(sozluk1,index=[0,1,2,3])
dataFrame2=pd.DataFrame(sozluk2,index=[4,5,6,7])
dataFrame3=pd.DataFrame(sozluk3,index=[8,9,10,11])
print(dataFrame1)
print("\n")
print(dataFrame2)
print("\n")
print(dataFrame3)
print("\n")
birlesmisFrame=pd.concat([dataFrame1,dataFrame2,dataFrame3],axis=0)#concat methoduna sırasıyla dataFramelerimizi koyarak birleştirebiliriz. axis=1 dediğimizde kolon birleştirmeside yapabiliriz
print(birlesmisFrame)
