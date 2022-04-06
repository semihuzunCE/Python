import numpy as np
dizi=[[10,20,30],[40,50,60],[70,80,90]]
matrix=np.array(dizi)
matrix[1,2]#matrix[1][2] ile aynı işlevde
print(f"{matrix} \n")
print(matrix[1:,1:]) # satırda ve sütunda 1 den sonraki indexleri bastır
print("\n")
print(matrix[[2,0,1,1]]) #Bu gösterimde indexleri liste biçiminde verdiğimizde verdiğimiz indexteki satırları sırasıyla bastırabiliriz