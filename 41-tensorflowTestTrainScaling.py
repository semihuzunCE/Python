from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt
#train_test_split
excelVerilerim=pd.read_excel("bisiklet_fiyatlari.xlsx")
# y = wx + b
# y-> label
# x-> feature
y=excelVerilerim["Fiyat"].values #fiyatların dizisini y ye atadık. values demezsek pandas olur dersek np dizisi olur 
x=excelVerilerim[["BisikletOzellik1","BisikletOzellik2"]].values
x_train, x_test, y_train , y_test = train_test_split(x,y,test_size=0.33,random_state=15) # x ve y değeri bizim label ve featurelarımızı tutar, test size verimizin ne kadarlık kısmı teste ayrılmalı onu gireriz random_state ise içine herhangi bir değer girebiliriz bizle aynı verileri kullanan biriyle aynı değeri girersek yakın sonuç almamız beklenir
print(x_train.shape) #670 veri train aşamasında
print(x_test.shape) #330 veri ise teste atandı
print(x_test)
#SCALING...............................................................................................................
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train) #scaler verimizi uygun hale getirmek için aayarlıyor

x_train=scaler.transform(x_train) #verimizi 0-1 arasında olacak şekilde oranlıyor
x_test=scaler.transform(x_test)

print(x_test)
#MODEL OLUŞTURMA.......................................................................................................
import tensorflow as tf 
from tensorflow.keras.models import Sequential # modelimizi oluşturmaya yarıyor
from tensorflow.keras.layers import Dense # katmanlarımızı oluşturmaya yarıyor
 
model = Sequential() #modelimizi oluşturduk
model.add(Dense(5,activation="relu")) # bu kodda ise gizli katmanlarımızı ekliyoruz sayısını belirlediğimiz kadarıyla. "5" nöron sayısını belirtir
model.add(Dense(5,activation="relu"))
model.add(Dense(5,activation="relu"))

model.add(Dense(1)) # bu kısımda çıkış katmanını oluşturuyoruz 

model.compile(optimizer= "rmsprop", loss= "mse")# yaptıklarımızı birleştiriyor. optimizera gradient descentta bahsettigimiz fonksiyonları kullanıyoruz genelde diğeri "adam" loss ada regresyon tipini giriyoruz
model.fit(x_train,y_train,epochs=250)
print(model.history.history) #loss değerlerini sözlük şeklinde değerlerini döndürür
loss=model.history.history["loss"] #şeklinde sözlük olan ifadeyi diziye çevirerek değişkene atadık
sbn.lineplot(x=range(len(loss)),y=loss)
plt.show()

trainLoss=model.evaluate(x_train,y_train,verbose=0)    #loss değerlerini değerlendirir. verbose=1 dersek biraz daha detaylı bilgi çıkarır
testLoss=model.evaluate(x_test,y_test,verbose=0)
print(f"trainimiz: {trainLoss}  testimiz:{testLoss}") # bu değerlerin yakın çıkması beklenir

testTahminleri = model.predict(x_test) #x_testte verilen özelliklere göre bir fiyat tahmini çıkaracak tahminleri numpy diziye atacak. Bizde bu tahminleri y_testteki gerçek fiyatlarla kıyaslayacağız
tahminDf=pd.DataFrame(y_test,columns=["Gerçek Y"]) #gerçek ve tahmin y değerlerimizi dataframe e atıp karşılaştıralım
testTahminleri=pd.Series(testTahminleri.reshape(330,)) #tahminleri seriese dönüştürerek data frame e ekleyebiliriz
tahminDf["Tahmin Y"]=testTahminleri #tahmini tesleride dataframe e ekleyerek değerlendirme yapabiliriz
print(tahminDf)

from sklearn.metrics import mean_absolute_error,mean_squared_error
absoluteHata=mean_absolute_error(tahminDf["Gerçek Y"],tahminDf["Tahmin Y"])
meanHata=mean_squared_error(tahminDf["Gerçek Y"],tahminDf["Tahmin Y"])
print(f"Ortalama hatamız{absoluteHata}\n squared hatamız:{meanHata}") #absolute hatamız 8-9 lira civarı çıkıyor yani yani tahminlerle gerçek değerler arası 8-9 lira fark çıkıyor. Bizim tahminlerimiz için bu fark iyi bir değerdir
print(excelVerilerim.describe())

#Elimize ulaşan bir veriyi modele tahmin ettirme
YeniBisiklet=[[1749.628226,1749.590668]]
YeniBisiklet=scaler.transform(YeniBisiklet) #veriyi daha küçük sayılara çeviriyor
print(f"yeni bisiklet tahminimiz: {model.predict(YeniBisiklet)}") #modelimize verimizi vererek fiyat tahmininde bulundurtuyoruz

#modelimizi kayıt etmek
from tensorflow.keras.models import load_model
model.save("bisiklet_modeli.h5")