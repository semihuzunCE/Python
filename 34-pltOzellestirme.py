import numpy as np
import matplotlib.pyplot as plt

dizi1=np.linspace(0,10,20) #0-10 arası 20 tane eşit aralıklı asyı seç
dizi2=dizi1**3
'''
plt.plot(dizi1,dizi2,"g--") #"g*-"  gibi özelliştirmelerde mevcut"
#plt.show()

plt.subplot(1,2,1) # 1 sıra olacak, 2 kolon olacak, 1. yi çizdiriyorum. Bu kısımda 1 den fazla grafiği aynı anda bastırmayı görüyoruz. subplot bize hem figure hem eksen döndürür tuple formatında
plt.plot(dizi1,dizi2,"g--")
plt.subplot(1,2,2)
plt.plot(dizi2,dizi1,"b*-")
plt.show()
'''
#kendi figure' ümüzü oluşturma
benimFigure=plt.figure() # bu kısım içi boş bir fügure oluşturur
figureAxes=benimFigure.add_axes([0.2,0.2,0.5,0.5]) # ilk iki girdi sırasıyla x ve y ekseninde grafiği kaydırmaya yarıyor son iki girdi ise grafiğin sırasıyla genişlik ve yüksekliğini belirtir
figureAxes.plot(dizi1,dizi2,"g--")
figureAxes.set_xlabel("x ekseni ismi")
figureAxes.set_ylabel("y ekseni ismi")
figureAxes.set_title("grafik başlıgı")
plt.show()


