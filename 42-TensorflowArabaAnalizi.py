import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
dataFrame=pd.read_excel("merc.xlsx")
print(dataFrame.head())
print(dataFrame.describe())
print(dataFrame.isnull().sum()) #verimizde hangi satırda ne kadar null veri var diye bakabiliriz

sbn.displot(dataFrame["price"]) #veri setimizde çok pahalı arabalar grafiği bozuyor
#plt.show()

dataFrame.corr() #data framedeki kolonların birbiriyle ilişkisini ortaya çıkartır
print(dataFrame.corr()["price"].sort_values())# bizim için fiyatı etkileyen faktörler daha önemli sadece onu küçükten büyüğe bastırabiliriz
#verimizde transmission sayısal olmadıgı için verimizde gözükmüyor. Onu hesaba katmadan hesabımızı yaptırcaz

print(dataFrame.sort_values("price",ascending=False).head(20)) #en yüksek fiyatlı 20 arabayı azalan sırada gösterdik
#elimizdeki araclardan yüzde 1 pahalı olanı (131 tane) çıkartıp daha düzgün bir grafik elde etmek istiyoruz:

DüzenliDf=dataFrame.sort_values("price",ascending=False).iloc[131:] # bu kodda sıraladıgımız df deki 131 den sonrasını yeni df ye eşitleyerek ilk 131 pahalı aracı yoksaymış olduk
sbn.displot(DüzenliDf["price"]) # ilk figüre göre daha düzenli oldugunu görebiliriz
#plt.show()
dataFrame=DüzenliDf #dataframedende istemediğimiz verileri çıkardık dataframe üzerinden işlem yapalım
print(dataFrame.groupby("year").mean()["price"]) #dataFrame'imizde 1970 teki araçların fiyatı beklenenin çok üstünde. Muhtemelen klasik araba filan var bu yıldaki araçları da çıkartmak isteyebiliriz.
print(dataFrame[dataFrame.year!=1970].groupby("year").mean()["price"]) # 1970 ler hariç diğer yıllardaki araçların ortalama fiyatını basar

dataFrame=dataFrame[dataFrame.year != 1970] # yazarak 1970 teki araçları çıkartabiliriz
print(dataFrame.groupby("year").mean()["price"])

dataFrame = dataFrame.drop("transmission", axis=1) #bu komutlada numerik olmayan kolonu droplayarak verimizi regresyona hazır hale getirmiş oluruz



#VERİMİZİ TEMİZLEDİK: Sıradaki adımlar: 1. np dizilerimizi oluşturacaz 2.sklearn kullanrak test ve train splitlerimizi oluşturacaz 3. Scaling yapıcaz 4. modelimizi oluşturup eğiteceğiz

#1. AŞAMA NP dizilerimizi oluşturalım

y=dataFrame["price"].values # tahminler sonucu ulaşmamız gereken değer y dir bizim projemizde bu fiyattır
x=dataFrame.drop("price",axis=1).values # x ise özelliklerdir. price hariç diğer kolonlar özelliklerimizi oluşturut


#2. AŞAMA sklearn kullanarak test ve train splitlerimizi uluşturacağız.

from sklearn.model_selection import train_test_split

x_train,x_test,y_train, y_test=train_test_split(x,y,test_size=0.30,random_state=10)
print(f"x_train veri adedi: {len(x_train)}\n x_test veri adedi:{len(x_test)}")

#3. AŞAMA Scaling işlemi
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
x_train=scaler.fit_transform(x_train) #önceki örnekte önce fit sorna transform yapmıştık. Şimdi ikisini tek seferde yapıyoruz.
x_test=scaler.transform(x_test)
#fiyatı yani y değerini scale etmemize gerek yok

#4. AŞAMA. TF kullanrak modelimizi oluşturalım

from tensorflow.keras.models import Sequential #model için
from tensorflow.keras.layers import Dense # katmanlar için
x_train.shape # print edersek (9090, 5) sonucuna ulaşırız 5 özellikli 9090 veri demek 5 katmandan başlatabiliriz
model = Sequential()

model.add(Dense(12,activation="relu")) # 4 gizli katman 12 nöronlu. Nöron sayısını biraz deneme yanılmayla bulabiliriz. aktivasyon fonksiyonu ise en işlevlilerden biri relu oldugu için onu koyuyoruz
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))

model.add(Dense(1)) #çıkış katmanı 1 tane ekliyoruz

model.compile(optimizer="adam",loss="mse") # model olarak "adam" kullanıyoruz en işlevsel optimizerlardan loss oalrakta öncekinde oldugu gibi "mse" yi kullanalım

model.fit(x=x_train,y=y_train,validation_data=(x_test,y_test),batch_size=250,  epochs=100) # validation_data kısmı modelin historyisine baktığımızda loss la birlikte val_loss değerinide beraber getirir. Yorumlama kısmını bizim için kolaylaştırır
kayipVerisi=pd.DataFrame(model.history.history)
kayipVerisi.plot()
#plt.show() # loss(kayıp) ve val_loss(doğrulama kaybı) değerlerinin gitgide azalması ve birbirine yakın olması beklenir. epoch değerini fazla verdiysek olabilir ya da modeli değiştirmek gerekebilir bu durumu düzeltmek için.
#!!!!!ONEMLI:loss değerlerinin ayrık olması overfeed durumunda test verilerimizde yakın tahminlerde bulunur ancak. Modele sonradan yaptıgımız tahminlerde kötü sonuç bulabilir

#5.AŞAMA Modeli yorumlama ve hatalara bakma
from sklearn.metrics import mean_absolute_error,mean_squared_error
tahminDizisi=model.predict(x_test) #testteki verileri vererek modele tahminde bulundurtuyoruz. Tahminleride dizimize atıyoruz. Bu tahminleride y_test le yani doğru fiyatlarla karşılaştırabiliriz

print(mean_absolute_error(y_test,tahminDizisi)) # 3100 civarı bir sonuç çıkıyor. Yani fiyatla tahmin arasında 3100 civarı sapma olabilir demek. Bu fark bizim için önemliyse modelde değişiklik yapabiliriz
#Tahmin yapma
yeniAraba=[2019,10000,155,60,2.2]
yeniArabaSeries=pd.Series(yeniAraba)
yeniArabaSeries=scaler.transform(yeniArabaSeries.values.reshape(-1,5))
tahminFiyat=model.predict(yeniArabaSeries)
print(f"tahmini fiyatımız:{tahminFiyat}")
