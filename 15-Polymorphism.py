#iki classda aynı isimde fonksiyon tanımladık ve farklı çıktılar aldık
class Elma():
    def __init__(self,isim):
        self.isim=isim
    def bilgiVer(self):
        return self.isim+" 100 kaloridir"
class Muz():
    def __init__(self,isim):
        self.isim=isim
    def bilgiVer(self):
        return self.isim+" 150 kaloridir"
elma=Elma("elma")
muz=Muz("muz")
meyvelistesi=[elma,muz]
for meyve in meyvelistesi:
    print(meyve.bilgiVer())
        