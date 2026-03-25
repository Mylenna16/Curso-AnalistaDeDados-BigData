import pandas as pd

tmax = pd.Series([30,35,40,29,30,32,39])
tmin = pd.Series([20,23,25,27,10,15,28])

mediamax = tmax.mean()
mediamin = tmin.mean()

print(f"A amplitude é: {tmax-tmin}")
print(f"A media da temperatura máxima é: {mediamax:.2f}")
print(f"A media da temperatura mínima é: {mediamin:.2f}")