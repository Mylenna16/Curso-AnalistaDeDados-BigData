import pandas as pd

endereco_dados = 'bases\Financeira.csv'

#Criando o dataframe
df_financeira = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')

print('------ DADOS FINANCEIROS ------')
print(df_financeira.head())