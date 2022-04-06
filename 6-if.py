# if'in içine girdiğimizde bir tab boşluk bırakmak lazım
if 3>2:
    print("semih")
x=5
y=7
if x>y:
    print("{}, {} den büyüktür".format(x,y))
else:
    print("{}, {} den büyüktür" .format(y,x))
    #elif komutu birden çok durumu kontrol ederken kullanılabilir
if 3>1:
    print("1. kısım")
elif 4>2:
    print("2. kısım")
    #birden fazla durum kontrolü:
if 3>2 and 5>3:
    print("doğru koşullar")
    #boolean kullanımı
canlımı=True
if canlımı:
    print("canlı")
elif not canlımı:
    print("cansız")
    # in komutu 
adım="semih uzun"
if "semih" in adım:
    print("ismim semih")
else:
    print("isim bilinmiyor")

