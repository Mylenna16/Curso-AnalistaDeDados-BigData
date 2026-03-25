# Programa que calcula o peso ideal de acordo com sexo

altura = float(input("Digite a sua altura: "))
pesoidealh = (72.7*altura)-58
pesoidealm = (62.1*altura)-44.7

print(f"O peso ideal se você for um homem é: {pesoidealh:.2f} e o peso ideal se você for uma mulher é: {pesoidealm:.2F}")
