#pip install xlrd - Biblioteca para manipular aequivos xlrd
#pip install openpyxl - Biblioteca para manipular arquivos do excel

import pandas as pd

endereco_dados = 'bases\ENEM_2020_2023.xlsx'

#Criando o dataframe
df_enem = pd.read_excel(endereco_dados)

print('------ QUANTIDADE DE INSCRITOS NO ENEM 2020 A 2023 ------')
print(df_enem.head())
