import numpy as np
import pandas as pd
tahminList={"istanbul":[30,29,np.nan],"ankara":[20,np.nan,25],"izmir":[40,39,38]} #np.nan numpynin boş veriler için kullandıgı yapı
havaDurumu=pd.DataFrame(tahminList) #3 şehrin 3 günlük hava durumu tahmini verileri var
havaDurumu["Günler"]=["pazartesi","salı","Çarşamba"]
havaDurumu.set_index("Günler",inplace=True)
havaDurumu.dropna(axis=0) #komutu bir satırda nan varsa o satırı komple siliyor "axis=1 dediğimizde sütunda nan olanları siler"
print(havaDurumu)


tahminList2={"istanbul":[30,29,np.nan],"ankara":[20,np.nan,25],"izmir":[40,39,38],"antalya":[45,np.nan,np.nan]} 
havaDurumu2=pd.DataFrame(tahminList2) 
havaDurumu2["Günler"]=["pazartesi","salı","Çarşamba"]
havaDurumu2.set_index("Günler",inplace=True)
print(havaDurumu2.dropna(axis=1,thresh=2)) #thresh komutuyla kolonunda en az 2 tane temiz verisi(nan olmayan) olanları tuttuk
havaDurumu2.fillna("-") # bu komutla nan olan verilere istediğimiz değeri girebiliriz
print(havaDurumu.isnull()) #bu komutla nan değerleri görebiliriz boolean olarak

