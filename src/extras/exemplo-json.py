import json

exemplo = """
    {
        "pergunta": "Qual é o resultado da expressão 2 + 2?",
        "opcoes": ["5", "4", "11", "22"],
        "certa": "4"
    }
"""

questao = json.loads(exemplo)

print(questao['pergunta'])

opcoes = questao['opcoes']

for i, opcao in enumerate(opcoes, start=1):
    print(f"{i}) {opcao}")

resposta = int(input("Escolha uma opção [1-4]: "))
opcao_selecionada = opcoes[resposta - 1]
opcao_certa = questao['certa']

if opcao_selecionada == opcao_certa:
    print("Você acertou!!!")
else:
    print(f"Você errou. A resposta certa é {opcao_certa}")
