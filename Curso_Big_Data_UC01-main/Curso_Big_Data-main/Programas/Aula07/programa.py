#Programa que vê quanto o usuário recebe e verifica os descontos e salario liquido

valor = float(input("Digite o valor que recebe por hora: "))
hora = int(input("Quantas horas trabalhados por mês: "))
salariobruto = valor*hora
irrf = salariobruto*(11/100)
inss = salariobruto*(8/100)
sindicato = salariobruto*(5/100)
salarioliquido = salariobruto-(irrf+inss+sindicato)

print(f"O salario bruto é: {salariobruto:.2f}")
print(f"O desconto do irrf é:{irrf:.2f}")
print(f"O desconto do inss é: {inss:.2f}")
print(f"Pagou ao sindicato: {sindicato:.2f}")
print(f"O salario liquido é {salarioliquido:.2f}")