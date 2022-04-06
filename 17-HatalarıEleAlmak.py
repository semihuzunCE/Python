# try hatasız ise else ve finallye gider. try hatalı ise except ve finally e gider
while True:
    try:
        benimInt=int(input("numara giriniz: "))
    except:
        print("yanlış girdi verdiniz")
        continue
    else:
        print("teşekkürler")
        break
    finally:
        print("finally çağrıldı")
    