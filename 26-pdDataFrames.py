import numpy as np
import pandas as pd
data=np.random.randn(4,3)#4 e 3 lük rastgele verilik matrix oluşturduk
#data frame sözlüğün iki boyutlu hali gibi kolonlarada bi index verebilirzi
dataFrame=pd.DataFrame(data)
print(dataFrame)
print(f"\n {dataFrame[0]}") # şeklinde çağırırsak kolon olarak 0. kolonu çağırabiliriz
#bu gösterimde kolonlara ve indexlerine nasıl isim vereceğimizi görüyoruz
yeniFrame=pd.DataFrame(data,index=["ahmet","omer","huseyin","semih"],columns=["maas","calisma saati","yas"])
print(f"\n {yeniFrame}")
#sadece belirli kolon veya satırları getirme
print("\n")
print(yeniFrame[["maas","yas"]]) # Bu ifadede istenilen kolonları çağırmayı görebiliyoruz
print("\n")
print(yeniFrame.loc[["ahmet","semih"]]) # Bu ifadede ise satırları getirmeyi görüyoruz
print("\n")
print(yeniFrame.iloc[1])# Bu ifadede ise dataframlerin indexlerlede satırlara erişebildiğini görüyoruz

yeniFrame["emeklilik yasi"]=yeniFrame["yas"]+yeniFrame["yas"] # yeni kolon ekleme
print("\n {}".format(yeniFrame))
yeniFrame.drop("emeklilik yasi",axis=1) # axis 1 kolonlarda default olan 0 silincek indexi satırda arar. bu drop komutu değişikliği ana framede yapmaz kopyasını oluşturur bunu başka framee eşitlersek o framede emeklilik yası olmaz. Ana framde değişiklik yapmak istiyorsak axis girdisinden sonra inplace=True girdisinide eklemeliyiz
yeniFrame.loc["fatma"]=[0.312312,0.572,0.21,-1.23231]# şeklinde yeni satırda ekleyebiliriz
print(yeniFrame)
yeniFrame.loc["semih"]["yas"]# ifadesiyle istenilen ifadelerin kesişimini bulabiliriz

booleanframe=yeniFrame>0# bu ifade framedeki 0 dan büyük olan kısımları true küçükleri false olarak döndürür
print("\n {}". format(booleanframe))
print(yeniFrame[yeniFrame["yas"]>0])

yeniFrame.reset_index()#bu ifade framin indexlerini index isminde bir kolon oluşturarak oraya atıyor ve indexleri 0,1,2 diye değiştiriyor. ana frame üzerinde inplace komutunu koymazsak değişiklik yapmıyor
print(yeniFrame.reset_index())
#ındexlerimizi aşağıdaki listedeki isimlerle değiştirmek istediğimizi düşünelim:
yeniIndex=["ahm","omr","hus","smh","ftm"]
yeniFrame["yeni index"]=yeniIndex#öncelikle istediğimiz indexleri kolon olarak ekledik
yeniFrame.set_index("yeni index",inplace=True) #daha sonra bu komutla istediğimiz kolonu index yapabiliriz
print(yeniFrame)
