#Programa onde pede o nome, as notas e calcula as medias e mostra se está de recuperação, reprovado e aprovado

nome = input("Digite seu nome: ")
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1+n2)/2

if media >= 7:
    print(f"{nome}, aprovado pois sua média foi {media:.2f}")
elif media >=3 and media <7:
    print(f"{nome}, recuperação pois sua média foi {media:.2f}")
else:
    print(f"{nome}, reprovado pois sua média foi {media:.2f}")

