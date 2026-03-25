usuarios = ["Mylenna","Larissa","Guilherme","Anna","Milena"]
senhas = ["1234","1345","2345","3456","4567"]

nome = input("Informe o nome de acesso ao sistema: ")
for i in range(len(usuarios)):
    if usuarios[i] == nome:
        senha=input("Informe a senha de acesso: ")
        if senhas[i] == senha:
            resp = "Acesso liberado"
        else:
            resp = "Senha não confere"
        break
    else:
        resp = "Usuario não encontrado"
print(resp)
