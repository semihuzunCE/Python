#try kısmında hatalı bir kısım oldugunda except kısmı çalışır
while True:
    try:
        a=int(input("1. sayıyı giriniz..."))
        b=int(input("1. sayıyı giriniz..."))
        print(f"toplam sonucu: {a+b}")
    except:
        print("Sayıları düzgün giriniz..")
