#Programa que vê se o funcionário está qualificado para a aposentadoria ou não

import datetime
data_atual = datetime.date.today()
try:
    nome = input("Digite seu nome: ")
    nasc = int(input("Informe o ano de nascimento: "))
    ano = int(input("Informe o ano que entrou na empresa? "))
except ValueError:
    print("Verifique a entrada de dados")
else:
    idade = data_atual.year - nasc
    tempo = data_atual.year - ano

    if idade >= 65:
        print(f"{nome}Apto a Aposentadoria")
    elif tempo >= 30:
        print(f"{nome}Apto a Aposentadoria")
    elif idade >= 60 and tempo >=25:
        print(f"{nome}Apto a Aposentadoria")
    else:
        print(f"{nome}Inapto a Aposentadoria")