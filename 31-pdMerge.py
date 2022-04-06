import numpy as np
import pandas as pd
from pandas.core.reshape.merge import merge
sozluk1={"isim":["akif","şerif","yusuf","furkan"],
        "spor":["koşu","yüzme","koşu","basketbol"]}
sozluk2={"isim":["akif","şerif","yusuf","furkan"],
        "kalori":[250,300,100,150]}
dataFrame1=pd.DataFrame(sozluk1)
dataFrame2=pd.DataFrame(sozluk2)
print(dataFrame2)
print("\n")
print(dataFrame1)

mergeData=pd.merge(dataFrame1,dataFrame2,on="isim")# ortak kolonları olan iki dataframe in kolonlarını birleştirebiliriz on attribute'u ile ortak kolonu yazarak eksik kolonları birleştiriyor
print("\n")
print(mergeData)