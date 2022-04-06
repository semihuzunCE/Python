import numpy as np
import pandas as pd
CalisanBilgi={"Department":["Yazılım","Hukuk","Hukuk","Pazarlama","Pazarlama"],
      "Calisan Ismi":["Samet","Hüseyin","Şerif","Akif","Yusuf"],
      "Maas":[200,250,100,300,500]}
CalisanTablom=pd.DataFrame(CalisanBilgi)
print(CalisanTablom["Department"].unique()) #tekrar eden departmenları da 1 kere basar
print(CalisanTablom["Department"].nunique()) #unique departmen sayısını basar. çıktı: "3"
print(CalisanTablom["Department"].value_counts()) #departmanlarda kaçar tane eleman oldugunu basar
print("\n")
print(CalisanTablom)
print("\n")

def yeniMaas(maas):
    return maas * 1.2
CalisanTablom["Maas"]= CalisanTablom["Maas"].apply(yeniMaas) #tanımladıgımız fonksiyonu calisan tablomuzdaki maaslara uyguladık
print(CalisanTablom)
