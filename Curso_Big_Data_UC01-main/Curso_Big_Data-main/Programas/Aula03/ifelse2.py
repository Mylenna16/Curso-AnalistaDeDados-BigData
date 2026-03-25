#Programa que vê se o usuario é maior ou menor de 19 anos e usando elif 

idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Usuário menor que 18 anos")
elif idade == 18:
    print("Usuário com 18, falta pouco!")
elif idade > 65:
    print("Usuário idoso")
else:
    print("Acesso liberado")