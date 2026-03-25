qtdm = 0
qtdovcl = 0
sexo = []
cor_dos_olhos = []
cor_dos_cabelos = []
idade = []
resp = "s"

while resp == "s" or resp == "S":
    sexo.append(input("Digite o sexo do usuário: F para feminino e M para masculino: "))
    cor_dos_olhos.append(input("Informe a cor dos olhos A - Azuis, V - Verdes ou C - Castanhos: "))
    cor_dos_cabelos.append(input("Informe a cor dos cabelos L - Louros, P - Pretos ou C - Castanhos: "))
    idade.append(int(input("Digite a idade da pessoa: ")))
    resp = input("Deseja continuar? ")

for i in range(len(sexo)):
    if (sexo[i] == "f" or sexo[i] == "F") and (idade[i] >= 18 and idade[i] <=35):
        qtdm+=1
    if (cor_dos_olhos[i] == "V" or cor_dos_olhos[i] == "v") and (cor_dos_cabelos[i] == "l" or cor_dos_cabelos[i] == "L"):
        qtdovcl+=1

print(f"A media das idades dos habitantes é {(sum(idade)/len(idade)):.1f}")
print(f"A maior das idades dos habitantes é {max(idade)}")
print(f"A menor das idades dos habitantes é {min(idade)}")
print(f"A quantidade de mulheres com idade entre 18 a 35 anos é: {qtdm}")
print(f"A quantidade de pessoas que tem olhos verdes e cabelos louros é: {qtdovcl}")