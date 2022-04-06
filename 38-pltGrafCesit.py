import numpy as np
import matplotlib.pyplot as plt

dizi1=np.linspace(0,10,20) 
dizi2=dizi1**2

dizi3=np.random.randint(0,100,50)
plt.scatter(dizi1,dizi2) #nokta grafiği

plt.hist(dizi3) #histogram grafiği

