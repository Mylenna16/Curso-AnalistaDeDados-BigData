import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('---- OBTENDO DADOS ----')

# Importando a base de dados financeira.csv
endereco_dados = 'bases\Titanic.csv'

# Criando o DataFrame financeira
df_titanic = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_fare_age = df_titanic[['PassengerId','Name','Age','Fare','Survived']]

# Exibindo a base de dados financeira
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_titanic.head())
print(df_fare_age.head())

# Criando o array do valor da passagem e da idade
array_titanic_fare = np.array(df_titanic["Fare"])
array_titanic_age = np.array(df_titanic["Age"])

# Obtendo a média do valor da passagem e da idade
media_fare = np.mean(array_titanic_fare)
media_age = np.mean(array_titanic_age)

# Obtendo a mediana do valor da passagem e da idade
mediana_fare = np.median(array_titanic_fare)
mediana_age = np.median(array_titanic_age)

# Obtendo a distância entre a média e a mediana do valor da passagem e da idade
distancia_fare = abs((media_fare - mediana_fare) / mediana_fare) * 100
distancia_age = abs((media_age - mediana_age) / mediana_age) * 100

# Obtendo o máximo e o mínimo do valor da passagem e da idade
maximo_fare = np.max(array_titanic_fare)
maximo_age = np.max(array_titanic_age)
minimo_fare = np.min(array_titanic_fare)
minimo_age = np.min(array_titanic_age)

# Obtendo a amplitude do valor da passagem e da idade
amplitude_fare = maximo_fare - minimo_fare
amplitude_age = maximo_age - minimo_age

# Obtendo os Quartis da passagem e da idade - Método weibull
q1_titanic_fare = np.quantile(array_titanic_fare, 0.25, method='weibull')
q2_titanic_fare = np.quantile(array_titanic_fare, 0.50, method='weibull')
q3_titanic_fare = np.quantile(array_titanic_fare, 0.75, method='weibull')
iqr_titanic_fare = q3_titanic_fare - q1_titanic_fare

q1_titanic_age = np.quantile(array_titanic_age, 0.25, method='weibull')
q2_titanic_age = np.quantile(array_titanic_age, 0.50, method='weibull')
q3_titanic_age = np.quantile(array_titanic_age, 0.75, method='weibull')
iqr_titanic_age = q3_titanic_age - q1_titanic_age

# Identificando os outliers superiores e inferiores da passagem e da idade
limite_superior_fare = q3_titanic_fare + (1.5 * iqr_titanic_fare)
limite_inferior_fare = q1_titanic_fare - (1.5 * iqr_titanic_fare)

limite_superior_age = q3_titanic_age + (1.5 * iqr_titanic_age)
limite_inferior_age = q1_titanic_age - (1.5 * iqr_titanic_age)

# Filtrando o DataFrame titanic
df_titanic_fare_outliers_superiores = df_fare_age[df_fare_age['Fare'] > limite_superior_fare]
df_titanic_fare_outliers_inferiores = df_fare_age[df_fare_age['Fare'] < limite_inferior_fare]

df_titanic_age_outliers_superiores = df_fare_age[df_fare_age['Age'] > limite_superior_age]
df_titanic_age_outliers_inferiores = df_fare_age[df_fare_age['Age'] < limite_inferior_age]

# Obtendo as medidas de dispersão do valor da passagem e da idade
variancia_fare = np.var(array_titanic_fare)
distancia_var_fare = variancia_fare / (media_fare**2)
desvio_padrao_fare = np.std(array_titanic_fare)
coeficiente_var_fare = desvio_padrao_fare / media_fare

variancia_age = np.var(array_titanic_age)
distancia_var_age = variancia_age / (media_age**2)
desvio_padrao_age = np.std(array_titanic_age)
coeficiente_var_age = desvio_padrao_age / media_age

# Exibindo os dados sobre o valor das passagens
print("\n-- OBTENDO INFORMAÇÕES SOBRE AS PASSAGENS --")
print('Medidas de Tendência Central')
print(f"\nA média das passagens é {media_fare:.2f}")
print(f"A mediana das passagens é {mediana_fare:.2f}")
print(f"A distância entre a média e a mediana é {distancia_fare:.2f} %")
print(f"O menor valor das passagens é {minimo_fare:.2f}")
print(f"O maior valor das passagens é {maximo_fare:.2f}")
print(f"A amplitude dos valores das passagens é {amplitude_fare:.2f}")
print(f"O valor do q1 - 25% do valor das passagens é {q1_titanic_fare:.2f}")
print(f"O valor do q2 - 50% do valor das passagens é {q2_titanic_fare:.2f}")
print(f"O valor do q3 - 75% do valor das passagens é {q3_titanic_fare:.2f}")
print(f"O valor do iqr = q3 - q1 do valor das passagens é {iqr_titanic_fare:.2f}")
print(f"O limite inferior do valor das passagens é {limite_inferior_fare:.2f}")
print(f"O limite superior do valor das passagens é {limite_superior_fare:.2f}")
print(f"A variância das passagens é {variancia_fare:.2f}")
print(f"A distância da variância X média das passagens é {distancia_var_fare:.2f}")
print(f"O desvio padrão das passagens é {desvio_padrao_fare:.2f}")
print(f"O coeficiente de variação das passagens é {coeficiente_var_fare:.2f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_titanic_fare_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_titanic_fare_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_titanic_fare_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_titanic_fare_outliers_superiores)

# Exibindo os dados sobre as idades dos passageiros
print("\n-- OBTENDO INFORMAÇÕES SOBRE AS IDADES --")
print('Medidas de Tendência Central')
print(f"\nA média das idades é {media_age:.1f}")
print(f"A mediana das idades é {mediana_age:.1f}")
print(f"A distância entre a média e a mediana é {distancia_age:.1f} %")
print(f"O menor valor das idades é {minimo_age}")
print(f"O maior valor das idades é {maximo_age}")
print(f"A amplitude dos valores das idades é {amplitude_age}")
print(f"O valor do q1 - 25% do valor das idades é {q1_titanic_age:.2f}")
print(f"O valor do q2 - 50% do valor das idades é {q2_titanic_age:.2f}")
print(f"O valor do q3 - 75% do valor das idades é {q3_titanic_age:.2f}")
print(f"O valor do iqr = q3 - q1 do valor das idades é {iqr_titanic_age:.2f}")
print(f"O limite inferior do valor das idades é {limite_inferior_age:.2f}")
print(f"O limite superior do valor das idades é {limite_superior_age:.2f}")
print(f"A variância das idades é {variancia_age:.2f}")
print(f"A distância da variância X média das idades é {distancia_var_age:.2f}")
print(f"O desvio padrão das idades é {desvio_padrao_age:.2f}")
print(f"O coeficiente de variação das idades é {coeficiente_var_age:.2f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_titanic_age_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_titanic_age_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_titanic_age_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_titanic_age_outliers_superiores)

# Visualizando os dados sobre a renda e os valores de empréstimo
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Valores das Passagens e Idades')

# posição 01: Gráfico das passagens
df_titanic_fare_outliers_superiores_order = df_titanic_fare_outliers_superiores.sort_values(by='Fare',ascending=True)
plt.subplot(2,2,1)
plt.xticks([])  
plt.title('Acumulado dos Valores das Passagens')
plt.bar(df_titanic_fare_outliers_superiores_order['Name'],df_titanic_fare_outliers_superiores_order['Fare'])

# posição 02: Gráfico das idades
df_titanic_age_outliers_superiores_order = df_titanic_age_outliers_superiores.sort_values(by='Age',ascending=True)
plt.subplot(2,2,2)
plt.title('Acumulado dos Valores das Idades')
plt.barh(df_titanic_age_outliers_superiores_order['Name'],df_titanic_age_outliers_superiores_order['Age'])

# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
plt.title('Medidas Descritivas das Passagens')
plt.axis('off')
plt.text(0.1,0.9,f'Média das Passagens {media_fare:.2f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana das Passagens {mediana_fare:.2f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana das Passagens {distancia_fare:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor das Passagens {maximo_fare:.2f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor das Passagens {minimo_fare:.2f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média das Passagens {distancia_var_fare:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação das Passagens {coeficiente_var_fare:.2f}',fontsize=12)

# posição 04: Medidas descritivas das idades
plt.subplot(2,2,4)
plt.title('Medidas Descritivas das Idades')
plt.axis('off')
plt.text(0.1,0.9,f'Média das Idades {media_age:.2f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana das Idades {mediana_age:.2f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana das Idades {distancia_age:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor das Idades {maximo_age:.2f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor das Idades {minimo_age:.2f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média das Idades {distancia_var_age:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação das Idades {coeficiente_var_age:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()