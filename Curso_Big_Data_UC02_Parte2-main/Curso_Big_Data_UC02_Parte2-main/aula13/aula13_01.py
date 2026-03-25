import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_cvli = df_ocorrencias[['aisp','cvli']]
# df_rec_veiculo = df_rec_veiculo[df_rec_veiculo['ano'].isin([2022,2023])]
df_cvli = df_cvli.groupby(['aisp']).sum(['cvli']).reset_index()
#df_rec_veiculo_ano = df_ocorrencias[['aisp','ano','recuperacao_veiculos']]
#df_rec_veiculo_ano = df_rec_veiculo_ano.groupby(['ano']).sum(['recuperacao_veiculos']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_cvli.head())

# Criando o array dos roubos de veiculos
array_cvli = np.array(df_cvli["cvli"])

# Obtendo a média dos roubos de veiculos
media_cvli = np.mean(array_cvli)

# Obtendo a mediana dos roubos de veiculos
mediana_cvli = np.median(array_cvli)

# Obtendo a distância entre a média e a mediana dos roubos de veiculos
distancia_cvli = abs((media_cvli - mediana_cvli) / mediana_cvli) * 100

# Obtendo o máximo e o mínimo dos roubos de veiculos
maximo_cvli = np.max(array_cvli)
minimo_cvli = np.min(array_cvli)

# Obtendo a amplitude dos roubos de veiculos
amplitude_cvli = maximo_cvli - minimo_cvli

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_cvli = np.quantile(array_cvli, 0.25, method='weibull')
q2_cvli = np.quantile(array_cvli, 0.50, method='weibull')
q3_cvli = np.quantile(array_cvli, 0.75, method='weibull')
iqr_cvli = q3_cvli - q1_cvli

# Identificando os outliers superiores e inferiores dos roubos de veículos
limite_superior_cvli = q3_cvli + (1.5 * iqr_cvli)
limite_inferior_cvli = q1_cvli - (1.5 * iqr_cvli)

# Filtrando o DataFrame roubos de veículos
df_cvli_outliers_superiores = df_cvli[df_cvli['cvli'] > limite_superior_cvli]
df_cvli_outliers_inferiores = df_cvli[df_cvli['cvli'] < limite_inferior_cvli]

# Obtendo as medidas de dispersão dos roubos de veículos
variancia_cvli = np.var(array_cvli)
distancia_var_cvli = variancia_cvli / (media_cvli**2)
desvio_padrao_cvli = np.std(array_cvli)
coeficiente_var_cvli = desvio_padrao_cvli / media_cvli


# Exibindo os dados sobre os roubos de veiculos
print("\nOBTENDO INFORMAÇÕES SOBRE OS CRIMES VIOLENTOS LETAIS INTENCIONAIS - CVLI")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média dos CVLI é {media_cvli:.0f}")
print(f"A mediana dos CVLI é {mediana_cvli:.0f}")
print(f"A distância entre a média e a mediana dos CVLI é {distancia_cvli:.2f} %")
print(f"O menor valor dos CVLI é {minimo_cvli:.0f}")
print(f"O maior valor dos CVLI é {maximo_cvli:.0f}")
print(f"A amplitude dos valores dos CVLI é {amplitude_cvli:.0f}")
print(f"O valor do q1 - 25% dos CVLI é {q1_cvli:.0f}")
print(f"O valor do q2 - 50% dos CVLI é {q2_cvli:.0f}")
print(f"O valor do q3 - 75% dos CVLI é {q3_cvli:.0f}")
print(f"O valor do iqr = q3 - q1 dos CVLI é {iqr_cvli:.0f}")
print(f"O limite inferior dos CVLI é {limite_inferior_cvli:.0f}")
print(f"O limite superior dos CVLI é {limite_superior_cvli:.0f}")
print(f"A variância dos CVLI é {variancia_cvli:.0f}")
print(f"A distância da variância X média dos CVLI é {distancia_var_cvli:.0f}")
print(f"O desvio padrão dos CVLI é {desvio_padrao_cvli:.0f}")
print(f"O coeficiente de variação dos CVLI é {coeficiente_var_cvli:.0f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_cvli_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_cvli_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_cvli_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_cvli_outliers_superiores)

# Visualizando os dados sobre os roubos de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Crimes Violentos Letais Intencionais - CVLI',fontsize=20)


# posição 01: Gráfico dos Roubos de Veículos
plt.subplot(2,2,1)
plt.title('BoxPlot dos Crimes Violentos Letais Intencionais - CVLI')
plt.boxplot(array_cvli,vert=False,showmeans=True)

# posição 02: Histograma dos Roubos de Veículos
plt.subplot(2,2,2)
plt.title('Histograma dos Crimes Violentos Letais Intencionais - CVLI')
plt.hist(array_cvli,bins=100,edgecolor='black')

# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
df_cvli_outliers_superiores_order = df_cvli_outliers_superiores.sort_values(by='cvli',ascending=True)
plt.title('Ranking dos Batalhoes de PM com Outliers Superiores')
plt.barh(df_cvli_outliers_superiores_order['aisp'].astype(str),df_cvli_outliers_superiores_order['cvli'])
#plt.plot(df_rec_veiculo_ano['ano'].astype(str),df_rec_veiculo_ano['recuperacao_veiculos'])

# posição 04: Medidas descritivas dos Roubos de Veículos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos Crimes Violentos Letais Intencionais - CVLI')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos CVLI: {media_cvli:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana dos CVLI: {mediana_cvli:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana dos CVLI: {distancia_cvli:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor dos CVLI: {maximo_cvli:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor dos CVLI: {minimo_cvli:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média dos CVLI: {distancia_var_cvli:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação dos CVLI: {coeficiente_var_cvli:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()