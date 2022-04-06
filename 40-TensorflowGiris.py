import pandas as pd
import seaborn as sbn #matplotlibin üstüne çıkmış kütüphane
import matplotlib.pyplot as plt
excelVerilerim=pd.read_excel("bisiklet_fiyatlari.xlsx")
print(excelVerilerim.head()) #ilk 5 veriyi getirir
sbn.pairplot(excelVerilerim) # verilerimizi bölerek ayrı ayrı grafiklendirir
plt.show()

