liste=[5,10,15,20,25]
#numara 15 oldugunda fordan çıksın
for numara in liste:
    if numara==15:
        break
    print(numara)
#numara 15 oldugunda döngüyü sonraki aşamadan devam ettirir
for numara in liste:
    if numara==15:
        continue
    print(numara)
#bı kısımda ne yazcağımızı henüz bilmiyorsak pass i kullanabilirz böylelikle daha sonra yazabiliriz
for numara in liste:
    pass