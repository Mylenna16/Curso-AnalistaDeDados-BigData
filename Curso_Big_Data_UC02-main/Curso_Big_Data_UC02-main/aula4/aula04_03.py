import pandas as pd
# Criando uma função para formatar número
def formatar(valor):
    return "{:.2f}%".format(valor)
# Criando a Tabela Ocorrências
ocorrencias = [
    ['Rio de Janeiro',6775561,35000],
    ['Niteroi',515317,2500],
    ['São Gonçalo',1091737,15000],
    ['Duque de Caxias',924624,12000],
    ['Nova Iguaçu',821128,10000],
    ['Belford Roxo',513118,9000],
    ['São João de Meriti',471906,8500],
    ['Petrópolis',306678,1000],
    ['Volta Redonda',273988,2000],
    ['Campos dos Goytacazes',507548,4000],
]
# Criando as Colunas da Tabela Alunos
colunas = ['Município','Habitantes','Roubos']
# Criando o DataFrame
df_ocorrencias = pd.DataFrame(ocorrencias,columns=colunas)
# Exibindo os Dados
print("\n----- Tabela de Ocorrencias -----")
print(df_ocorrencias)
# Realizando os Cálculos
soma_roubos = df_ocorrencias['Roubos'].sum(axis=0)
media_roubos = df_ocorrencias['Roubos'].mean(axis=0)
soma_populacao = df_ocorrencias['Habitantes'].sum(axis=0)
media_populacao = df_ocorrencias['Habitantes'].mean(axis=0)
maior_roubos = df_ocorrencias['Roubos'].max(axis=0)
menor_roubos = df_ocorrencias['Roubos'].min(axis=0)
maior_populacao = df_ocorrencias['Habitantes'].max(axis=0)
menor_populacao = df_ocorrencias['Habitantes'].min(axis=0)
maior_municipio_roubos = df_ocorrencias[df_ocorrencias['Roubos'] == maior_roubos]['Município']
menor_municipio_roubos = df_ocorrencias[df_ocorrencias['Roubos'] == menor_roubos]['Município']
maior_municipio_populacao = df_ocorrencias[df_ocorrencias['Habitantes'] == maior_populacao]['Município']
menor_municipio_populacao = df_ocorrencias[df_ocorrencias['Habitantes'] == menor_populacao]['Município']
# tx_roubo = ((df_ocorrencias['Roubos'] / df_ocorrencias['Habitantes']) * 100).apply(formatar)
df_ocorrencias['Taxa'] = ((df_ocorrencias['Roubos'] / df_ocorrencias['Habitantes']) * 100).apply(formatar)

# Exibindo os Dados
print("\n---- Informações Solicitadas ----")
print(f"A quantidade total de roubos no período foi {soma_roubos}")
print(f"A quantidade média de roubos no período foi {media_roubos:.0f}")
print(f"A quantidade total de pessoas no Estado são {soma_populacao}")
print(f"A quantidade média de pessoas no Estado são {media_populacao:.0f}")
print(f"O maior valor de roubos no período foi {maior_roubos}")
print(f"O menor valor de roubos no período foi {menor_roubos}")
print(f"O maior valor populacional no Estado é {maior_populacao}")
print(f"O menor valor populacional no Estado é {menor_populacao}")
print(f"O município com maior quantidade de roubos é {maior_municipio_roubos}")
print(f"O município com menor quantidade de roubos é {menor_municipio_roubos}")
print(f"O município com maior valor populacional é {maior_municipio_populacao}")
print(f"O município com menor valor populacional é {menor_municipio_populacao}")
print("\n---- Taxa de Roubos ----")
print(df_ocorrencias[['Município','Taxa']])