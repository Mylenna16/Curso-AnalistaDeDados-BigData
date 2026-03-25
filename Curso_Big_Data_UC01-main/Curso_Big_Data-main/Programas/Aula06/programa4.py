usuarios = ["Mylenna","Larissa","Guilherme","Anna","Milena"]
senhas = ["1234","1345","2345","3456","4567"]

nome = input("Digite o nome da pessoa: ")
for i in range(len(usuarios)):
    if usuarios[i] == nome:
        resp = print("Usuário encontrado")
        break
    else:
        resp = print("Usuário não encontrado")


