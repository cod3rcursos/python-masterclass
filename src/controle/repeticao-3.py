pergunta = "Deseja continuar? (S/n) "
resposta = input(pergunta)
quatidade = 1

while resposta.lower() != "n":
    print(f"Vamos continuar pela {quatidade} vez")
    resposta = input(pergunta)

    quatidade = quatidade + 1

print("Fim do exemplo")