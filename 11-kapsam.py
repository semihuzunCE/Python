#normalde fonksiyon içindeki değişken dışardan bagımsızdır ancak dışardaki y yi kullanmak fonk. içinde değiştirmek istiyorsak fonk. içinde onun global oldugunu belirtmek lazım
y=10
def carpma():
    global y 
    y=5
    print(y)