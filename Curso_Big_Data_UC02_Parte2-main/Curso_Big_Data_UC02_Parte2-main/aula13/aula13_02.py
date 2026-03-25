import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_hom_doloso = df_ocorrencias[['cisp','hom_doloso']]
df_hom_doloso = df_hom_doloso.groupby(['cisp']).sum(['hom_doloso']).reset_index()

df_hom_doloso_culposo = df_ocorrencias[['cisp','hom_doloso','hom_culposo']]
df_hom_doloso_culposo = df_hom_doloso_culposo.groupby(['cisp']).sum(['hom_doloso','hom_culposo']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_hom_doloso.head())

# Criando o array dos roubos de veiculos
array_hom_doloso = np.array(df_hom_doloso["hom_doloso"])

# Obtendo a média dos roubos de veiculos
media_hom_doloso = np.mean(array_hom_doloso)

# Obtendo a mediana dos roubos de veiculos
mediana_hom_doloso = np.median(array_hom_doloso)

# Obtendo a distância entre a média e a mediana dos roubos de veiculos
distancia_hom_doloso = abs((media_hom_doloso - mediana_hom_doloso) / mediana_hom_doloso) * 100

# Obtendo o máximo e o mínimo dos roubos de veiculos
maximo_hom_doloso = np.max(array_hom_doloso)
minimo_hom_doloso = np.min(array_hom_doloso)

# Obtendo a amplitude dos roubos de veiculos
amplitude_hom_doloso = maximo_hom_doloso - minimo_hom_doloso

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_hom_doloso = np.quantile(array_hom_doloso, 0.25, method='weibull')
q2_hom_doloso = np.quantile(array_hom_doloso, 0.50, method='weibull')
q3_hom_doloso = np.quantile(array_hom_doloso, 0.75, method='weibull')
iqr_hom_doloso = q3_hom_doloso - q1_hom_doloso

# Identificando os outliers superiores e inferiores dos roubos de veículos
limite_superior_hom_doloso = q3_hom_doloso + (1.5 * iqr_hom_doloso)
limite_inferior_hom_doloso = q1_hom_doloso - (1.5 * iqr_hom_doloso)

# Filtrando o DataFrame roubos de veículos
df_hom_doloso_outliers_superiores = df_hom_doloso[df_hom_doloso['hom_doloso'] > limite_superior_hom_doloso]
df_hom_doloso_outliers_inferiores = df_hom_doloso[df_hom_doloso['hom_doloso'] < limite_inferior_hom_doloso]

# Obtendo as medidas de dispersão dos roubos de veículos
variancia_hom_doloso = np.var(array_hom_doloso)
distancia_var_hom_doloso = variancia_hom_doloso / (media_hom_doloso**2)
desvio_padrao_hom_doloso = np.std(array_hom_doloso)
coeficiente_var_hom_doloso = desvio_padrao_hom_doloso / media_hom_doloso

# Obtendo a correlação entre os homicídios
# 0,9 a 1,0 (positivo ou negativo): correlação muito forte;
# 0,7 a 0,9 (positivo ou negativo): correlação forte;
# 0,5 a 0,7 (positivo ou negativo): correlação moderada;
# 0,3 a 0,5 (positivo ou negativo): correlação fraca;
# 0,0 a 0,3 (positivo ou negativo): não possui correlação.
correlacao_hom = np.corrcoef(df_hom_doloso_culposo['hom_doloso'],df_hom_doloso_culposo['hom_culposo'])[0,1]

# Exibindo os dados sobre os roubos de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS HOMICÍDIOS DOLOSOS -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média dos homicídios dolosos é {media_hom_doloso:.0f}")
print(f"A mediana dos homicídios dolosos é {mediana_hom_doloso:.0f}")
print(f"A distância entre a média e a mediana é dos homicídios dolosos é {distancia_hom_doloso:.2f} %")
print(f"O menor valor dos homicídios dolosos é {minimo_hom_doloso:.0f}")
print(f"O maior valor dos homicídios dolosos é {maximo_hom_doloso:.0f}")
print(f"A amplitude dos valores dos homicídios dolosos é {amplitude_hom_doloso:.0f}")
print(f"O valor do q1 - 25% dos homicídios dolosos é {q1_hom_doloso:.0f}")
print(f"O valor do q2 - 50% dos homicídios dolosos é {q2_hom_doloso:.0f}")
print(f"O valor do q3 - 75% dos homicídios dolosos é {q3_hom_doloso:.0f}")
print(f"O valor do iqr = q3 - q1 dos homicídios dolosos é {iqr_hom_doloso:.0f}")
print(f"O limite inferior dos homicídios dolosos é {limite_inferior_hom_doloso:.0f}")
print(f"O limite superior dos homicídios dolosos é {limite_superior_hom_doloso:.0f}")
print(f"A variância dos homicídios dolosos é {variancia_hom_doloso:.0f}")
print(f"A distância da variância X média dos homicídios dolosos é {distancia_var_hom_doloso:.0f}")
print(f"O desvio padrão dos homicídios dolosos é {desvio_padrao_hom_doloso:.0f}")
print(f"O coeficiente de variação dos homicídios dolosos é {coeficiente_var_hom_doloso:.0f}")
print(f"A correlação dos homicídios é {correlacao_hom:.1f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_hom_doloso_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_hom_doloso_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_hom_doloso_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_hom_doloso_outliers_superiores)

# Visualizando os dados sobre os roubos de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Homicídios Dolosos')

# posição 01: Gráfico dos Roubos de Veículos
plt.subplot(2,2,1)
plt.title('BoxPlot dos Homicídios Dolosos')
plt.boxplot(array_hom_doloso,vert=False,showmeans=True)

# posição 02: Histograma dos Roubos de Veículos
plt.subplot(2,2,2)
plt.title('Comparativo Homicídios Dolosos e Culposos')
plt.scatter(df_hom_doloso_culposo['hom_doloso'],df_hom_doloso_culposo['hom_culposo'])
plt.xlabel('Homicídio Doloso')
plt.ylabel('Homicídio Culposo')

# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
df_hom_doloso_outliers_superiores_order = df_hom_doloso_outliers_superiores.sort_values(by='hom_doloso',ascending=True)
plt.title('Ranking das Delegacias')
plt.barh(df_hom_doloso_outliers_superiores_order['cisp'].astype(str),df_hom_doloso_outliers_superiores_order['hom_doloso'])

# posição 04: Medidas descritivas dos Roubos de Veículos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos Homicídios Dolosos')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos Homicídios Dolosos: {media_hom_doloso:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana dos Homicídios Dolosos: {mediana_hom_doloso:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana dos Homicídios Dolosos: {distancia_hom_doloso:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor dos Homicídios Dolosos: {maximo_hom_doloso:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor dos Homicídios Dolosos: {minimo_hom_doloso:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média dos dos Homicídios Dolosos: {distancia_var_hom_doloso:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação dos Homicídios Dolosos: {coeficiente_var_hom_doloso:.2f}',fontsize=12)
plt.text(0.1,0.2,f'Correlação entre os Homicídios: {correlacao_hom:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()