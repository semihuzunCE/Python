import numpy as np
import matplotlib.pyplot as plt

dizi1=np.linspace(0,10,20) 
dizi2=dizi1**3

fig1=plt.figure()


eksen1=fig1.add_axes([0.2,0.2,0.7,0.7])
eksen1.plot(dizi1,dizi2,"g")
eksen1.set_xlabel("x ekseni")
eksen1.set_ylabel("y ekseni")
eksen1.set_title("Ana Grafik")

eksen2=fig1.add_axes([0.3,0.5,0.2,0.2]) # küçük grafiğin ilk değeriyle oynayarak büyük grafiğin istediğimiz yerine ayarlayabiliriz
eksen2.plot(dizi2,dizi1,"g")
eksen2.set_xlabel("x ekseni")
eksen2.set_ylabel("y ekseni")
eksen2.set_title("Alt Grafik")
plt.show()


#subplot kullanarak aynısını yapalım.

(benimFigure, benimEksenler)=plt.subplots(nrows=1,ncols=2) # colon 2 yaptıgımız için eksenimiz 2 tane oluyor her bir eksene dizi şeklinde erişebiliriz
for eksen in benimEksenler:
    eksen.plot(dizi1,dizi2,"g")
    eksen.set_xlabel("x ekseni")
plt.tight_layout()#bu komut iki eksenimiz arasına mesafeyi birazcık açar yapışmasını önler
plt.show()