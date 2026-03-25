import pandas as pd

#Importando dados via web
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Ocorrências
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
print('\n---- OBTENDO DADOS GERAIS SOBRE OCORRÊNCIAS ----')
print(df_ocorrencias.head())

# Criando o DataFrame Roubo de Veículos por Município
df_roubo_veiculo = df_ocorrencias[['munic','roubo_veiculo']]
# Totalizando Roubo de Veículos por Município
df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
print('\n---- OBTENDO DADOS SOBRE ROUBOS DE VEÍCULOS ----')
print(df_roubo_veiculo.head())

# Criando o DataFrame Homicidio Doloso por Ano
df_ano_hom_doloso = df_ocorrencias[['ano','hom_doloso']]
# Totalizando Homicidio Doloso por Ano
df_ano_hom_doloso = df_ano_hom_doloso.groupby(['ano']).sum(['hom_doloso']).reset_index()
print('\n---- OBTENDO DADOS SOBRE HOMICÍDIO DOLOSO ----')
print(df_ano_hom_doloso.head())

# Criando o DataFrame Homicidio Doloso e Culposo por Delegacias
df_cisp_dol_culp = df_ocorrencias[['cisp','hom_doloso','hom_culposo']]
# Totalizando Homicidio Doloso e Culposo por Delegacias
df_cisp_dol_culp = df_cisp_dol_culp.groupby(['cisp']).sum(['hom_doloso','hom_culposo']).reset_index()
print('\n---- OBTENDO DADOS SOBRE HOMICÍDIO DOLOSO E CULPOSO ----')
print(df_cisp_dol_culp.head())