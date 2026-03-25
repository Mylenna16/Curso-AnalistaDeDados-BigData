#Programa que pega dois números e divive eles e corrige o erro da divisão por 0

try:
    n1 = int(input("Informe o primeiro valor inteiro: "))
    n2 = int(input("Informe o segundo valor inteiro: "))
except ValueError:
    print("Verifique a entrada de dados")
else:
    try:
        result = n1/n2
    except ZeroDivisionError:
        print("Não é possível dividir por 0")
    else:
        print(result)