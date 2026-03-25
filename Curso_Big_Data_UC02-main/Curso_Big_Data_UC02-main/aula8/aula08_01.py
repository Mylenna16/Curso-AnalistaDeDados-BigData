import pandas as pd
import numpy as np

# Importando a Base de Dados
endereco_dados = 'bases\Funcionarios.csv'

# Criando o DataFrame 
df_funcionarios = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')

# Exibindo a base de dados funcionarios
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_funcionarios.head())

# Criando o array do salário e das idades dos funcionários
array_salario = np.array(df_funcionarios["Salário"])
array_idade = np.array(df_funcionarios["Idade"])

# Obtendo a média do salário e das idades dos funcionários
media_salario = np.mean(array_salario)
media_idade = np.mean(array_idade)

# Obtendo a mediana do salário e das idades dos funcionários
mediana_salario = np.median(array_salario)
mediana_idade = np.median(array_idade)

# Obtendo a distância entre a média e a mediana do salário e das idades dos funcionários
distancia_salario = abs((media_salario - mediana_salario) / mediana_salario) * 100
distancia_idade = abs((media_idade - mediana_idade) / mediana_idade) * 100

# Obtendo o máximo e o mínimo do valor do salário e das idades dos funcionários
maximo_salario = np.max(array_salario)
minimo_salario = np.min(array_salario)
maximo_idade = np.max(array_idade)
minimo_idade = np.min(array_idade)

# Obtendo a amplitude do valor do salário e das idades dos funcionários
amplitude_salario = maximo_salario - minimo_salario
amplitude_idade = maximo_idade - minimo_idade

# Exibindo os dados solicitados sobre os salários dos funcionários
print("\n-- OBTENDO INFORMAÇÕES SOBRE OS SALÁRIOS DOS FUNCIONÁRIOS --")
print(f"A média dos salários é R$ {media_salario:.2f}")
print(f"A mediana dos salários é R$ {mediana_salario:.2f}")
print(f"A distância entre a média e a mediana é {distancia_salario:.2f} %")
print(f"O menor valor dos salários é R$ {minimo_salario:.2f}")
print(f"O maior valor dos salários é R$ {maximo_salario:.2f}")
print(f"A amplitude dos valores dos salários é {amplitude_salario:.2f}")

# Exibindo os dados solicitados sobre as idades dos funcionários
print("\n-- OBTENDO INFORMAÇÕES SOBRE AS IDADES DOS FUNCIONÁRIOS --")
print(f"A média das idades é {media_idade:.1f}")
print(f"A mediana das idades é {mediana_idade:.1f}")
print(f"A distância entre a média e a mediana é {distancia_idade:.1f} %")
print(f"O menor valor das idades é {minimo_idade}")
print(f"O maior valor das idades é {maximo_idade}")
print(f"A amplitude dos valores das idades é {amplitude_idade}")