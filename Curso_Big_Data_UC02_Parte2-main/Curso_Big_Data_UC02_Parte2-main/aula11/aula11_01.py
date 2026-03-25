import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_veiculo = df_ocorrencias[['cisp','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['cisp']).sum(['roubo_veiculo']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_roubo_veiculo.head())

# Criando o array dos roubos de veiculos
array_roubo_veiculo = np.array(df_roubo_veiculo["roubo_veiculo"])

# Obtendo a média dos roubos de veiculos
media_roubo_veiculo = np.mean(array_roubo_veiculo)

# Obtendo a mediana dos roubos de veiculos
mediana_roubo_veiculo = np.median(array_roubo_veiculo)

# Obtendo a distância entre a média e a mediana dos roubos de veiculos
distancia_roubo_veiculo = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo) * 100

# Obtendo o máximo e o mínimo dos roubos de veiculos
maximo_roubo_veiculo = np.max(array_roubo_veiculo)
minimo_roubo_veiculo = np.min(array_roubo_veiculo)

# Obtendo a amplitude dos roubos de veiculos
amplitude_roubo_veiculo = maximo_roubo_veiculo - minimo_roubo_veiculo

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
q2_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.50, method='weibull')
q3_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.75, method='weibull')
iqr_roubo_veiculo = q3_roubo_veiculo - q1_roubo_veiculo

# Identificando os outliers superiores e inferiores dos roubos de veículos
limite_superior_roubo_veiculo = q3_roubo_veiculo + (1.5 * iqr_roubo_veiculo)
limite_inferior_roubo_veiculo = q1_roubo_veiculo - (1.5 * iqr_roubo_veiculo)

# Filtrando o DataFrame roubos de veículos
df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior_roubo_veiculo]
df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior_roubo_veiculo]

# Obtendo as medidas de dispersão dos roubos de veículos
variancia_roubo_veiculo = np.var(array_roubo_veiculo)
distancia_var_roubo_veiculo = variancia_roubo_veiculo / (media_roubo_veiculo**2)
desvio_padrao_roubo_veiculo = np.std(array_roubo_veiculo)
coeficiente_var_roubo_veiculo = desvio_padrao_roubo_veiculo / media_roubo_veiculo



# Exibindo os dados sobre os roubos de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS ROUBOS DE VEÍCULOS -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média dos roubos de veículos é {media_roubo_veiculo:.0f}")
print(f"A mediana dos roubos de veículos é {mediana_roubo_veiculo:.0f}")
print(f"A distância entre a média e a mediana é dos roubos de veículos é {distancia_roubo_veiculo:.2f} %")
print(f"O menor valor dos roubos de veículos é {minimo_roubo_veiculo:.0f}")
print(f"O maior valor dos roubos de veículos é {maximo_roubo_veiculo:.0f}")
print(f"A amplitude dos valores dos roubos de veículos é {amplitude_roubo_veiculo:.0f}")
print(f"O valor do q1 - 25% dos roubos de veículos é {q1_roubo_veiculo:.0f}")
print(f"O valor do q2 - 50% dos roubos de veículos é {q2_roubo_veiculo:.0f}")
print(f"O valor do q3 - 75% dos roubos de veículos é {q3_roubo_veiculo:.0f}")
print(f"O valor do iqr = q3 - q1 dos roubos de veículos é {iqr_roubo_veiculo:.0f}")
print(f"O limite inferior dos roubos de veículos é {limite_inferior_roubo_veiculo:.0f}")
print(f"O limite superior dos roubos de veículos é {limite_superior_roubo_veiculo:.0f}")
print(f"A variância dos roubos de veículos é {variancia_roubo_veiculo:.0f}")
print(f"A distância da variância X média dos roubos de veículos é {distancia_var_roubo_veiculo:.0f}")
print(f"O desvio padrão dos roubos de veículos é {desvio_padrao_roubo_veiculo:.0f}")
print(f"O coeficiente de variação dos roubos de veículos é {coeficiente_var_roubo_veiculo:.0f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_roubo_veiculo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_veiculo_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_roubo_veiculo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_roubo_veiculo_outliers_superiores)

# Visualizando os dados sobre os roubos de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Roubos de Veículos')

# posição 01: Gráfico dos Roubos de Veículos
plt.subplot(2,2,1)
plt.title('BoxPlot dos Roubos de Veículos')
plt.boxplot(array_roubo_veiculo,vert=False,showmeans=True)

# posição 02: Histograma dos Roubos de Veículos
plt.subplot(2,2,2)
plt.title('Histograma dos Roubos de Veículos')
plt.hist(array_roubo_veiculo,bins=100,edgecolor='black')

# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
df_roubo_veiculo_outliers_superiores_order = df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo',ascending=True)
plt.title('Ranking das Delegacias com Outliers Superiores')
plt.barh(df_roubo_veiculo_outliers_superiores_order['cisp'].astype(str),df_roubo_veiculo_outliers_superiores_order['roubo_veiculo'])

# posição 04: Medidas descritivas dos Roubos de Veículos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos Roubos de Veículos')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos Roubos de Veículos {media_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana dos Roubos de Veículos {mediana_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana dos Roubos de Veículos {distancia_roubo_veiculo:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor dos Roubos de Veículos {maximo_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor dos Roubos de Veículos {minimo_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média dos Roubos de Veículos {distancia_var_roubo_veiculo:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação dos Roubos de Veículos {coeficiente_var_roubo_veiculo:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()