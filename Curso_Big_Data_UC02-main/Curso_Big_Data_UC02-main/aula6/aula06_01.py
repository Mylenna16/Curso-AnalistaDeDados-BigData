import pandas as pd

endereco_dados = 'bases/Funcionarios.csv'

#Criando o dataframe
df_funcionarios = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

print(df_funcionarios.head())

media_salarial = df_funcionarios['Salário'].mean(axis=0)
media_idade = df_funcionarios['Idade'].mean(axis=0)
menor_t = df_funcionarios['Tempo'].min(axis=0)
maior_t = df_funcionarios['Tempo'].max(axis=0)
media_tc = df_funcionarios['Tempo'].mean(axis=0)
maior_idd = df_funcionarios['Idade'].max(axis=0)
menor_idd = df_funcionarios['Idade'].min(axis=0)
fun_n = df_funcionarios[df_funcionarios['Idade'] == menor_idd]['Nome']
fun_v = df_funcionarios[df_funcionarios['Idade'] == maior_idd]['Nome']
total_fun = df_funcionarios['Nome'].count()
maior_salario = df_funcionarios['Salário'].max(axis=0)
fun_msa = df_funcionarios[df_funcionarios['Salário'] == maior_salario]['Nome']
fun_mt = df_funcionarios[df_funcionarios['Tempo'] == maior_t]['Nome']


print(f"A media salarial é {media_salarial:.2f}")
print(f"A media das idades é {media_idade:.2f}")
print(f"Menor tempo de casa é {menor_t}")
print(f"Maior tempo de casa é {maior_t}")
print(f"Diferença entre o maior e o menor tempo de casa {maior_t-menor_t}")
print(f"A media de tempo de casa é {media_tc:.2f}")
print(f"Funcionario mais novo é {fun_n.values[0]}")
print(f"Funcionario mais velho é {fun_v.values[0]}")
print(f"A diferença de idades entre eles é {maior_idd-menor_idd}")
print(f"O total de funcionários é {total_fun}")
print(f"Funcionario com maior salario é {fun_msa.values[0]}")
print(f"Funcionario com mais tempo de casa é {fun_mt.values[0]}")