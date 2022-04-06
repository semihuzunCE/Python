from random import randint
from random import shuffle
liste=[1,2,3,4,5,6,7,8,9]
# range methodu başlangıç bitiş ve atlamada değeri alır ya da sadece bitiş değeri alır alttaki örnekte range bize 0-19 arası bir liste oluşturur
print(list(range(20)))
for numara in list(range(10)):
    print(numara)
#enumarete bize listenin indexini ve değerini aynı anda verir bunu tuple formatında verir
for eleman in enumerate(list(range(10))):
    print(eleman)
#randint() fonksiyonu bize içine girilen aralıkta rastgele bir int verir
print(randint(0,100))
#shuffle fonksiyonu içine verilen listeyi karıştırır
print(liste)
shuffle(liste)
print(liste)
# zip içine koyulan listeleri indexlerine göre tuple formatında birleştirir koyulan listelerden en az elemana hangisi sayipse o kadar tuple oluşturur
liste1=["pztesi","salı","cuma"]
liste2=["elma","armut","muz"]
liste3=[100,200,300]
print(list(zip(liste1,liste2,liste3)))
#adımdaki her bir elemanı listeye atıyoruz tuhaf bir gösterim. Altta ismin her harfini 2 kez ekliyor 
adım="semih uzun"
liste4=[eleman*2 for eleman in adım]
print(liste4)

