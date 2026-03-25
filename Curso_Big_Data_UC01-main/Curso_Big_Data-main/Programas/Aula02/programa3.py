# Programa que efetua o calculo do valor de uma prestação em atraso

tempo = int(input("Digite o tempo: "))
prestacao = float(input("Digite a prestação: "))
taxa = float(input("Digite a taxa: "))
valorfinal = prestacao+(prestacao*(taxa/100)*tempo)

print(f"O valor final é: R${valorfinal:.2f}")