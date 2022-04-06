import numpy as np 
import pandas as pd
from sklearn import preprocessing
from sklearn.utils import validation
from tensorflow.python.keras import callbacks
from tensorflow.python.keras.engine import sequential

dataFrame=pd.read_excel("maliciousornot.xlsx")
print(dataFrame.corr()["Type"].sort_values())

import matplotlib.pyplot as plt
import seaborn as sbn

sbn.countplot(x="Type",data=dataFrame)
#plt.show()

y=dataFrame["Type"].values
x=dataFrame.drop("Type",axis=1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.30,random_state=15)
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

scaler.fit(x_train)
X_train=scaler.transform(x_train)
X_test=scaler.transform(x_test)
import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation,Dropout
from tensorflow.keras.callbacks import EarlyStopping
model=Sequential()
model.add(Dense(units=30,activation="relu"))
model.add(Dropout(0.6)) #nöronları girilen yüzde kadar kapatır ve açar
model.add(Dense(units=15,activation="relu"))
model.add(Dropout(0.6))
model.add(Dense(units=15,activation="relu"))
model.add(Dropout(0.6))
model.add(Dense(units=1,activation="sigmoid"))

model.compile(loss="binary_crossentropy",optimizer="adam")

earlyStopping=EarlyStopping(monitor="val_loss",mode="min",verbose=1,patience=25) #val_loss çok artamya başladıgında epochsları bitirir
model.fit(x=X_train,y=y_train,epochs=700,validation_data=(X_test,y_test),verbose=1,callbacks=[earlyStopping]) #callback kısmına earlystoppingi koyarak ordaki işlemleri gerçekleştiririz

modelKaybı=pd.DataFrame(model.history.history)
modelKaybı.plot()
#plt.show()

tahminler=(model.predict(X_test) > 0.5).astype("int32") #tahminleri 1 ya da 0 a dönüştürüyor

print(tahminler)
from sklearn.metrics import classification_report,confusion_matrix


print(classification_report(y_test,tahminler)) # sınıflandırma sonucunda doğruluk oranı gibi değerleri bastırıyor

print(confusion_matrix(tahminler,y_test)) #confusion matrixini bastırıyor