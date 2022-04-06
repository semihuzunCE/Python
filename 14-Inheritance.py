#kedi sınıfına Hayvanı gödnererek onun methodlarına ve constructoruna erişimi sağlandı
class Hayvan():
    def __init__(self):
        print("Hayvan sınıfı çağrıldı")
    def method1(self):
        print("method1 çağrıldı")
    def method2(self):
        print("method2 çağrıldı")
class Hayvan2():
    def __init__(self):
        print("Hayvan 2 çağrıldı")
class Kedi(Hayvan,Hayvan2):
    def __init__(self):
        Hayvan.__init__(self)
        Hayvan2.__init__(self)
        print("kedi sınıfı çağrıldı")
        #override yaparak kedi sınıfında da method 1 tanımladık
    def method1(self):
        print("kedi sınıfındaki method 1 çağrıldı")
        
Goril=Hayvan()
scootish=Kedi()
scootish.method1()
Goril.method1()

