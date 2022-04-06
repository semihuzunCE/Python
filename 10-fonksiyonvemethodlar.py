
def ilkfonksiyon():
    print("ilk fonksiyonum")
def merhabadünya(yazdır):
    print(yazdır)
hello="hello world"
merhabadünya(hello)

def toplam(num1,num2):
    return num1+num2
print(toplam(20,5))
# args ve kwargs
# *args girdisini verdiğimizde istediğimizkadar girdi ekleyebilriz. return args ise bize tuple döndürür
def yenitoplam(*args):
    return sum(args)
print(yenitoplam(5,3,5,7,4,6))
# kwargs ise anahtar kelime yani sözlük oluşturabiliriz. İstediğimiz kadar argüman ekleyebilrizi.
def örnekfonksiyon(**kwargs):
    return kwargs
sozluk=dict()
sozluk=örnekfonksiyon(muz=100,elma=200)
print(sozluk)

def keykontrol(**kwargs):
    if "muz" in kwargs:
        print("kelime mevcut")
    else:
        print("kelime mevcut değil")

keykontrol(**sozluk)