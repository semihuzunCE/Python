import numpy as np
import pandas as pd
#Multi indexlemede 2 tane indeximiz olacak. Ana index ikinci indexlerin bir kısmını kapsıcak
ilkIndexler=["Monkey D.","Monkey D.","Monkey D.","Uchiha","Uchiha","Uchiha"]
ikinciIndexler=["Luffy","Dragon","Garp","Madara","Itachi","Sasuke"]
yasGuc=np.array([[20,"A"],[45,"S"],[70,"S"],[75,"S"],[30,"A"],[25,"S"]]) #dataframe'in içeriği
indexBirlestir=list(zip(ilkIndexler,ikinciIndexler))#bu kısımda ilk ve ikinci indexleri 2şer gruplama yapıyoruz
indexBirlestir=pd.MultiIndex.from_tuples(indexBirlestir) # bu kısımda indexbirlestir içindeki tuplestaki ikili verilerin ilk kısmı ilkindexleri tutuyor bunlarda aynı olan kısımlar teke indirgeniyor
animeListem=pd.DataFrame(yasGuc,index=indexBirlestir,columns=["Yas","Güc"]) #MultiIndex Methoduyla oluşturdugumuz ikili indexi dataframe'e verdiğimizde otomatik olarak ilk indexlerden altalta aynı olanları grupluyor 
print(animeListem)
print(animeListem.loc["Uchiha"])# şeklinde sadece uchihalara erişebiliriz
print(animeListem.loc["Monkey D."].loc["Luffy"]) # şeklinde monkey D. lerden sadece luffye erişebiliriz
animeListem.index.names=["Aile","İsim"] #ifadesiyle index kolonlarına isim verebiliriz
print(animeListem)
