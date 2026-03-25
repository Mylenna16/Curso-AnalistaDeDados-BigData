import pandas as pd

maria = pd.Series([800,700,1000,900,1200,600,600])
joao = pd.Series([900,500,1100,1000,900,500,700])
manoel = pd.Series([700,600,900,1200,900,700,400])

print("\nInformações sobre a vendedora Maria -")
print(f"O total de vendas é:{maria.sum():.2f}")
print(f"O total da média é:{maria.mean():.2f}")
print(f"O total da média é:{maria.max():.2f}")
print(f"O total da média é:{maria.min():.2f}")

print("\nInformações sobre o vendedor João -")
print(f"O total de vendas é:{joao.sum():.2f}")
print(f"O total da média é:{joao.mean():.2f}")
print(f"O total da média é:{joao.max():.2f}")
print(f"O total da média é:{joao.min():.2f}")

print("\nInformações sobre o vendedor manoel -")
print(f"O total de vendas é:{manoel.sum():.2f}")
print(f"O total da média é:{manoel.mean():.2f}")
print(f"O total da média é:{manoel.max():.2f}")
print(f"O total da média é:{manoel.min():.2f}")