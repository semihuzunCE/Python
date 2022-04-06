import numpy as np
#range fonksiyonunun np.array versiyonu. Örnekte arrayimize 0 dan 100 e sayıları 5 er aralıkla ekletiyoruz
print(np.arange(0,100,5))
#içine girilen sayı adedince 0 olan ve 1 olan fonksiyonlar. Aynı zamanda çift boyutluda tanımlanabilir
np.ones(5)
np.zeros((2,2))#2 ye 2 lik içinde 0 olan array
#0 ile 20 arasında 6 sayı seç ve aralıkları aynı olsun"0 ve 20 dahil"
print(np.linspace(0,20,6))
#birim matrix oluşturur. İçine verdiğimiz değer kaça kaçlık matrix oldugunu gösterir
print(np.eye(7))
#np nin random fonksiyonları:
np.random.randn(5) #5 tane rastgele sayı np dizisi olarak döner
np.random.randint(1,10,5)#1-10 arası "10 dahil değil" sayı döndürür sondaki 5 i yazdıgımızda 5 sayı döndürüp np dizisi olarak döner yoksa tek sayı




