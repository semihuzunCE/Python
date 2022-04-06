#init fonksiyonu constructor görevinde
#metodları tanımlarken içine self yazmak gerekli. Bunu yazmazsak selfe ait değişkenlere ulaşamayız
class SuperKahraman():
    def __init__(self,isim,yas,meslek):
        print("init çağrıldı")
        self.isim=isim
        self.yas=yas
        self.meslek=meslek
    def ornekmethod(self):
        print(f"ben süper kahramanım ve adım {self.isim}")
batman=SuperKahraman("batman",37,"İs Adamı")
print(batman.isim)
batman.ornekmethod()
#aşağıdaki tanımlamada constructora değer girmezsek default olarak 5 olarak yaşa atar
class Kopek():
    def __init__(self,yas=5) -> None:
        self.yas=yas
    def insanyasi(self):
        print(f"kopeğimizin insan yaşı: {self.yas*7}")

karabas=Kopek(7)
print(karabas.yas)
karabas.insanyasi()