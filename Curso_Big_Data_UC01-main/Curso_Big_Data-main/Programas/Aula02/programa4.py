#Programa que calcula a idade de nascimento de uma pessoa pelo ano de nascimento dela

import datetime

dataatual = datetime.date.today()
anoatual= dataatual.year
mesatual = dataatual.month
diaatual = dataatual.day
anon = int(input("Digite o ano que você nasceu: "))
idade = anoatual-anon

#print(dataatual) exemplo datetime data
#print(anoatual) exemplo datetime ano
#print(mesatual) exemplo datetime mes
#print(diaatual) exemplo datetime dia
#print(f"{diaatual}/{mesatual}/{anoatual}") exemplo de colocar no formato brasileiro ***existe uma função para configuração***

print(f"A sua idade é: {idade}")