import numpy as np
from numpy.lib import npyio
npDizim=np.arange(30)
#reshape fonksiyonu diziyi istediğimiz satır sütun sayısına göre bölüyor
npYeniden=npDizim.reshape(6,5)
print(npYeniden)
#ddizideki max ve min elemanı döndürür diğer ikiside indexi dönürür
npYeniden.max()
npYeniden.min()
npYeniden.argmax()
npYeniden.argmin()

