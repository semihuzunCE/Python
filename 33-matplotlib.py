import numpy as np
import matplotlib.pyplot as plt
yasListesi=[10,20,30,40,50,60,70,80,90,100]
kiloListesi=[15,70,85,95,60,65,75,87,55,65]
numpyKiloListesi=np.array(kiloListesi)
numpyYasListesi=np.array(yasListesi)

plt.plot(numpyYasListesi,numpyKiloListesi,"r") #ilk girdi x ekseni ikinci y ekseni, üçüncü olan grafigin rengi
plt.xlabel("Yas")
plt.ylabel("Kilo")
plt.title("Yaşlara göre kilo grafiği")
plt.show()