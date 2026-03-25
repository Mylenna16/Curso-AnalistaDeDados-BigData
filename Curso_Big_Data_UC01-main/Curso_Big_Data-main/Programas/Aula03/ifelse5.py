#Programa que vê se os valores são iguais ou diferentes e soma e multiplica

n1 = int(input("Informe o primeiro valor inteiro: "))
n2 = int(input("Informe o segundo valor inteiro: "))

if n1==n2:
    print(f"Os valores são iguais, então o produto é {n1*n2}")
else:
    print(f"Os valores são diferentes, então a soma é {n1+n2}")