# Programa que calcula o peso ideal de acordo com sexo com seu if e else

altura = float(input("Digite a sua altura: "))
sexo = input("Digite seu sexo, F - para feminino e M - para masculino ")

if sexo == "F" or "f":
    pesoidealm = (62.1*altura)-44.7
    print(f"O seu peso ideal é: {pesoidealm:.2f}")
elif sexo == "M" or "m":
    pesoidealh = (72.7*altura)-58
    print(f"O seu peso ideal é: {pesoidealh:.2f}")
else:
    print("Verifique o sexo informado")









