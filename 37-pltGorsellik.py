import numpy as np
import matplotlib.pyplot as plt

dizi1=np.linspace(0,10,20) 
dizi2=dizi1**2

(fig,eksen)=plt.subplots()
eksen.plot(dizi1,dizi2,"g",color="#3A95A8",linestyle="--") # hexadecimal kodlarla renk ayarı yapabiliriz.linestyle çizgi stilini ayarlar
eksen.plot(dizi2,dizi1,"r",alpha=0.1,linewidth=3.0) # alpha değeri saydamlık katar. linewidth ise çizgi kalınlığı katar
plt.show()