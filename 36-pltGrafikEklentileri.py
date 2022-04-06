import numpy as np
import matplotlib.pyplot as plt

dizi1=np.linspace(0,10,20) 
fig1=plt.figure()
eksen=fig1.add_axes([0.2,0.2,0.5,0.5])
eksen.plot(dizi1,dizi1**2,"r",label="dizi1**2")
eksen.plot(dizi1,dizi1**3,"g",label="dizi1**3")
eksen.legend(loc=1) # bu komut figure de çizgilerin hangi labele karşılık geldiğini göstermemize yarar. loc komutu labellerin grafiğin hangi köşesinde çıkcagını belirtir
plt.show()
# fig1.savefig("deneme.png",dpi=20) #dpi komutu grafiğin çözünürlüğünü ayarlar