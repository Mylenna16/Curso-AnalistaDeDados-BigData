import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

# Endereço dos dados
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')

# Filtrando os dados para os anos de 2021, 2022, 2023 e 2024
df_ocorrencias = df_ocorrencias[df_ocorrencias['ano'].isin([2021, 2022, 2023, 2024])]
print("Exibe os anos em: 2021, 2022, 2023, 2024")

# Agrupando e somando as lesões corporais dolosas e culposas
df_lesao_dolosa = df_ocorrencias.groupby(['cisp']).sum(['lesao_corp_dolosa']).reset_index()
df_lesao_culposa = df_ocorrencias.groupby(['cisp']).sum(['lesao_corp_culposa']).reset_index()

# Exibindo a base de dados
print('\n---- EXIBINDO A BASE DE DADOS ----')
print(df_lesao_dolosa.head())

# Análise estatística das lesões corporais dolosas
array_lesao_corp_dolosa = np.array(df_lesao_dolosa["lesao_corp_dolosa"])
media_lesao_corp_dolosa = np.mean(array_lesao_corp_dolosa)
mediana_lesao_corp_dolosa = np.median(array_lesao_corp_dolosa)
maximo_lesao_corp_dolosa = np.max(array_lesao_corp_dolosa)
minimo_lesao_corp_dolosa = np.min(array_lesao_corp_dolosa)

# Identificando outliers
q1_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.25)
q3_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.75)
iqr_lesao_corp_dolosa = q3_lesao_corp_dolosa - q1_lesao_corp_dolosa
limite_superior_lesao_corp_dolosa = q3_lesao_corp_dolosa + (1.5 * iqr_lesao_corp_dolosa)

# Análise estatística das lesões corporais culposas
array_lesao_corp_culposa = np.array(df_lesao_culposa["lesao_corp_culposa"])
media_lesao_corp_culposa = np.mean(array_lesao_corp_culposa)
mediana_lesao_corp_culposa = np.median(array_lesao_corp_culposa)
maximo_lesao_corp_culposa = np.max(array_lesao_corp_culposa)
minimo_lesao_corp_culposa = np.min(array_lesao_corp_culposa)

# Identificando outliers para lesões corporais culposas
q1_lesao_corp_culposa = np.quantile(array_lesao_corp_culposa, 0.25)
q3_lesao_corp_culposa = np.quantile(array_lesao_corp_culposa, 0.75)
iqr_lesao_corp_culposa = q3_lesao_corp_culposa - q1_lesao_corp_culposa
limite_superior_lesao_corp_culposa = q3_lesao_corp_culposa + (1.5 * iqr_lesao_corp_culposa)

# Exibindo as informações estatísticas
print("\n--------- OBTENDO INFORMAÇÕES SOBRE AS LESÕES CORPORAIS DOLOSAS -----------")
print(f"A média das lesões corporais dolosas é {media_lesao_corp_dolosa:.0f}")
print(f"A mediana das lesões corporais dolosas é {mediana_lesao_corp_dolosa:.0f}")
print(f"O menor valor das lesões corporais dolosas é {minimo_lesao_corp_dolosa:.0f}")
print(f"O maior valor das lesões corporais dolosas é {maximo_lesao_corp_dolosa:.0f}")

print("\n--------- OBTENDO INFORMAÇÕES SOBRE AS LESÕES CORPORAIS CULPOSAS -----------")
print(f"A média das lesões corporais culposas é {media_lesao_corp_culposa:.0f}")
print(f"A mediana das lesões corporais culposas é {mediana_lesao_corp_culposa:.0f}")
print(f"O menor valor das lesões corporais culposas é {minimo_lesao_corp_culposa:.0f}")
print(f"O maior valor das lesões corporais culposas é {maximo_lesao_corp_culposa:.0f}")

# Observando as DPs com maiores registros
maiores_registros_dolosa = df_lesao_dolosa.nlargest(5, 'lesao_corp_dolosa')
maiores_registros_culposa = df_lesao_culposa.nlargest(5, 'lesao_corp_culposa')

# Exibindo as DPs que mais registraram ocorrências
print('\nObservando as DPs que registraram os maiores registros de lesões corporais dolosas:')
print(maiores_registros_dolosa[['cisp', 'lesao_corp_dolosa']])

print('\nObservando as DPs que registraram os maiores registros de lesões corporais culposas:')
print(maiores_registros_culposa[['cisp', 'lesao_corp_culposa']])

# Analisando DPs com valores discrepantes (outliers)
outliers_dolosa = df_lesao_dolosa[df_lesao_dolosa['lesao_corp_dolosa'] > limite_superior_lesao_corp_dolosa]
outliers_culposa = df_lesao_culposa[df_lesao_culposa['lesao_corp_culposa'] > limite_superior_lesao_corp_culposa]

# Exibindo DPs com outliers
print('\nDPs com valores discrepantes (lesões corporais dolosas):')
if not outliers_dolosa.empty:
    outliers_dolosa_sorted = outliers_dolosa.sort_values(by='lesao_corp_dolosa', ascending=False)
    print(outliers_dolosa_sorted[['cisp', 'lesao_corp_dolosa']])
else:
    print("Não existem DPs com valores discrepantes para lesões corporais dolosas.")

print('\nDPs com valores discrepantes (lesões corporais culposas):')
if not outliers_culposa.empty:
    outliers_culposa_sorted = outliers_culposa.sort_values(by='lesao_corp_culposa', ascending=False)
    print(outliers_culposa_sorted[['cisp', 'lesao_corp_culposa']])
else:
    print("Não existem DPs com valores discrepantes para lesões corporais culposas.")

# Visualizando os dados
plt.subplots(2, 2, figsize=(16, 7))
plt.suptitle('Análise dos Dados sobre Lesões Corporais')

# Gráfico 1: BoxPlot das lesões corporais dolosas
plt.subplot(2, 2, 1)
plt.title('BoxPlot das Lesões Corporais Dolosas')
plt.boxplot(array_lesao_corp_dolosa, vert=False, showmeans=True)

# Gráfico 2: Histograma das lesões corporais dolosas
plt.subplot(2, 2, 2)
plt.title('Histograma das Lesões Corporais Dolosas')
plt.hist(array_lesao_corp_dolosa, bins=100, edgecolor='black')

# Gráfico 3: BoxPlot das lesões corporais culposas
plt.subplot(2, 2, 3)
plt.title('BoxPlot das Lesões Corporais Culposas')
plt.boxplot(array_lesao_corp_culposa, vert=False, showmeans=True)

# Gráfico 4: Histograma das lesões corporais culposas
plt.subplot(2, 2, 4)
plt.title('Histograma das Lesões Corporais Culposas')
plt.hist(array_lesao_corp_culposa, bins=100, edgecolor='black')

# Exibindo o Painel
plt.tight_layout()
plt.show()