import pandas as pd

s1 = pd.Series([80,90,10,40,20,40,50,90,20,50])
s2 = pd.Series([70,40,20,10,40,50,60,80,30,90])

print("Soma:")
print(s1+s2)
print("Subtração:")
print(s1-s2)
print("Multiplicação:")
print(s1*s2)
print("Divisão:")
print(s1/s2)