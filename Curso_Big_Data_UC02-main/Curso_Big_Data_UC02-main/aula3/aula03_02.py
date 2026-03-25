import pandas as pd

# Criando uma função para formatar número
def formatar(valor):
    return "{:.2f}%".format(valor)
    
# Criando o Código
roubo = pd.Series([100,90,80,120,110,90,70])
furto = pd.Series([80,60,70,60,100,50,30])
recuperacao = pd.Series([70,50,90,80,100,70,50])

roubofurto = roubo+furto
tx_recuperacao = ((recuperacao/roubofurto)*100).apply(formatar)
print("\nTotal geral de roubos -")
print(f"{roubofurto.sum()}")
print("\nTotal de roubos diários -")
print(f"{roubofurto}")
print("\nTaxa de recuperação diária -")
print(f"{tx_recuperacao}")