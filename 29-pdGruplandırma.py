import numpy as np
import pandas as pd
CalisanBilgi={"Department":["Yazılım","Yazılım","Hukuk","Hukuk","Pazarlama","Pazarlama"],
      "Calisan Ismi":["Samet","Ömer","Hüseyin","Şerif","Akif","Yusuf"],
      "Maas":[200,250,900,100,300,500]}
CalisanTablom=pd.DataFrame(CalisanBilgi)
print(CalisanTablom)

groupbyDep=CalisanTablom.groupby("Department") #department'a göre groupby yapıp objemize eşitledik
print(groupbyDep.count()) #departmanlarda kaç kişi çalıştıgını bastırabiliriz
print(groupbyDep.mean()) #sayısal değerlerin ortalamasını basar
print(groupbyDep.max()) #departmanlardaki max maas alan kişiyi ve maasını basar 
print(groupbyDep.describe()) #departmanlardaki max maaş min maaş, ortalama gibi bir çok bilgiyi aynı anda verir