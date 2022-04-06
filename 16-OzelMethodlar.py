#bunların hepsine magic methods diye aratarak bulabiliriz
class Meyve():
    def __init__(self,isim,kalori):
        self.isim=isim
        self.kalori=kalori
    def __str__(self):
        return f"{self.isim} kalori miktarı: {self.kalori}"
    def __len__(self):
        return self.kalori

muz=Meyve("muz",150)
#burdaki print adres basar. Ancak __str__() fonksiyonununda printini istediğimiz gibi yapabiliriz
print(muz)
# normalde leni kullanamıyorduk bile ama classta tanımlayarak istediğimiz çıktıyı alabiliriz
print(len(muz))
