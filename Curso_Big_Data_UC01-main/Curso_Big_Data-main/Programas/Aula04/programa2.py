#Programa que pega o produto, a quantidade e preço para ver o total e quem está apto ao desconto

produto = (input("Digite o nome do produto: "))
quant = int(input("Digite a quantidade do produto: "))
precou = float(input("Digite o preço do produto: "))
total = quant*precou

print(f"O valor total sem desconto é: {total}")
if quant <=5:
    desconto = total*0.98
    print(f"O total a pagar pelo {produto} é: {desconto} ")
elif quant > 5 and quant <=10:
    desconto = total*0.97
    print(f"O total a pagar pelo {produto} é: {desconto} ")
else:
    desconto = total*0.95
    print(f"O total a pagar pelo {produto} é: {desconto} ")

    
