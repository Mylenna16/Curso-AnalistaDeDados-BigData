import pandas as pd

# Criando uma função para formatar número
def formatar(valor):
    return "{:.2f}%".format(valor)
    
# Criando o Código
popv = pd.Series([30000000, 25000000, 10000000, 5000000])
popt = pd.Series([213317639, 214477744, 215574303, 216687971])

taxa = ((popv/popt)*100).apply(formatar)
print("\n----Dados vacinação----")
print(f"A quantidade total de pessoas vacinadas é: {sum(popv)} e a média é {popv.mean()}")
print("\n----Dados população----")
print(f"A quantidade total da população brasileira é: {sum(popt)} e a média é {popt.mean()}")
print(f"A taxa de vacinação anual nos últimos 4 anos é: {taxa}")