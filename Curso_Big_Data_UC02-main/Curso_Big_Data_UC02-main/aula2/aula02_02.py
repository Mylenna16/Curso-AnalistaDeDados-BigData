#Codigo usando séries

import pandas as pd

media = pd.Series([80,90,10,40,20,40,50,90,20,50])
ap = media[media >= 70]
rep = media[media < 70]
print("Medias maiores que 70:")
print(ap)
print("Medias menores que 70:")
print(rep)