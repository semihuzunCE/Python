#listedeki elemanları sırayla rakama atıyor
listem=[1,2,3,4,5,6]
for rakam in listem:
    if rakam%2==0:
        print(rakam)
liste2=[(2,5),(5,6),(7,9)]
for (x,y) in liste2:
    print(x," ",y)

x=0
while x<10:
    print(x)
    x+=1
# bu kısımda listede 3 oldugu sürece çalışır
while 3 in listem:
    print("3 hala listede")
    listem.pop()
