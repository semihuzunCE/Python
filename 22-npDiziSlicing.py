import numpy as np
a=np.arange(30)
a[3:6]=-1 #3 ten 6. indexe kadar olan verileri değiştirebiliriz.com
Dizim=np.arange(5,100,5)
DizimParcam=Dizim[0:5]
DizimParcam[:]=5#bu komutla tüm elemanları değiştiririz ve parçasını aldıgımız dizide de bu değişikliği görürüz ana dizide değişiklik istemiyorsak copy ile işlem yapmalıyız
DizimCopy=Dizim.copy()
DizimParcam2=DizimCopy[6:10]
DizimParcam2[:]=3
print(DizimParcam2)
print(DizimCopy)
print(Dizim)