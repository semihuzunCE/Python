import numpy as np
import pandas as pd
# pandas serileri sözlük mantıgıyla çalışıyor
sozluk={"Semih" : 22,"Huseyin" : 29,"omer" : 26}
seri=pd.Series(sozluk)
print(seri)
#yukardaki ve aşağıdaki gösterim iki farklı series oluşturma yöntemi
yaslarım=[20,22,36]
isimler=["hüso","samet","omer"]
seri2=pd.Series(index=isimler,data=yaslarım) #bu kısımda index veya data olarak belirtmezsek ilk kısım data ikinci kısımı ındex olarak alır
print(f"\n{seri2}")
#np dizilerininden de series oluşturabiliriz
npDizim=np.arange(20,30)
seri3=pd.Series(npDizim) # seriye tek değer verirsek onu dataya atar indexlerinide otomatik 0dan başlatır
print(f"\n{seri3}")
#serileri toplarsak aynı indextekileri toplar
yarısSeri1=pd.Series([1,5,8],["Omer","Semih","Huseyin"])
yarısSeri2=pd.Series([1,4,2],["Omer","Huseyin","Semih"])
print(yarısSeri1+yarısSeri2)

yeniAraba=[2019,10000,155,60,2.2]
yeniArabaSeries=pd.Series(yeniAraba)
print(type(yeniArabaSeries.values))
