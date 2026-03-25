import pandas as pd
# Criando a Tabela Vendedores
vendedores = [
    ['Ana','F',28,120],
    ['Bruno','M',34,150],
    ['Carlos','M',45,110],
    ['Diana','F',30,95],
    ['Eduardo','M',40,130],
    ['Fernanda','F',29,140],
    ['Gustavo','M',38,105],
    ['Helena','F',31,125],
    ['Igor','M',27,100],
    ['Juliana','F',33,135],
]
# Criando as Colunas da Tabela Alunos
colunas = ['Nome','Sexo','Idade','Vendas']
# Criando o DataFrame
df_vendedores = pd.DataFrame(vendedores,columns=colunas)
# Exibindo os Dados
print("\n--- Tabela de Vendedores ---")
print(df_vendedores)
# Realizando os Cálculos
soma_vendas = df_vendedores['Vendas'].sum(axis=0)
media_vendas = df_vendedores['Vendas'].mean(axis=0)
media_idades = df_vendedores['Idade'].mean(axis=0)
maior_idades = df_vendedores['Idade'].max(axis=0)
menor_idades = df_vendedores['Idade'].min(axis=0)
maior_vendas = df_vendedores['Vendas'].max(axis=0)
menor_vendas = df_vendedores['Vendas'].min(axis=0)
maior_nome = df_vendedores[df_vendedores['Vendas'] == maior_vendas]['Nome']
menor_nome = df_vendedores[df_vendedores['Vendas'] == menor_vendas]['Nome']
QTD_vendas_M = df_vendedores[df_vendedores['Sexo'] == 'M']['Vendas'].sum(axis=0)
QTD_vendas_F = df_vendedores[df_vendedores['Sexo'] == 'F']['Vendas'].sum(axis=0)
# Exibindo os Dados
print("\n---- Informações Solicitadas ----")
print(f"A quantidade total de vendas no período foi {soma_vendas}")
print(f"A quantidade média de vendas no período foi {media_vendas:.0f}")
print(f"A média das idades dos vendedores é {media_idades:.0f} anos.")
print(f"A maior das idades dos vendedores é {maior_idades} anos.")
print(f"A menor das idades dos vendedores é {menor_idades} anos.")
print(f"O nome do vendedor com mais vendas é {maior_nome.values[0]}")
print(f"O nome do vendedor com menos vendas é {menor_nome.values[0]}")
print(f"A quantidade de vendas do sexo masculino foi {QTD_vendas_M}")
print(f"A quantidade de vendas do sexo feminino foi {QTD_vendas_F}")