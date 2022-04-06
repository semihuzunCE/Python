import numpy as np
dizi=np.random.randint(1,100,20)
#dizideki değerlerin 25ten büyük olup olmadıgını boolean şeklinde bastırabiliriz 
print(dizi>25)
YeniDizi=dizi>25 #dizideki 25ten büyük olan kısımları yeni diziye atabiliriz
print(dizi[dizi>50]) # bu şekilde de print edebiliriz ya da başka diziye atabiliriz
YeniDizi=np.arange(0,51) 
print(YeniDizi*YeniDizi)# şeklinde direk o diziyi başka diziyle veya kendisiyle toplama çıkarma çarpma gibi işlemler yapabilrizi
