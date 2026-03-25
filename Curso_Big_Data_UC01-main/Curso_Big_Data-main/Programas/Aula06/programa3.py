nomes = []
medias = []
resp = "S"
while resp == "S" or resp == "s":
    nomes.append(input("Informe o nome do estudante: ")) #append é para guardar a informação na lista
    medias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja continuar? ")
for i in range(len(medias)):
    print(i,"- ",nomes[i], " - ",medias[i])
    maior_media = max(medias)
    pos = medias.index(maior_media)
    print(f"{nomes[pos]}, você possui a maior média")
    print(f"A media da turma é {(sum(medias)/len(medias)):.1f}")
    print(f"A maior media da turma é {max(medias)}")
    print(f"A menor media da turma é {min(medias)}")
    print(f"A amplitude da média da turma é {max(medias)-min(medias)}")
    medias.sort()
    # codigo para fazer com que fique decrescente: medias.sort(reverse="false") 
    print(medias)
   