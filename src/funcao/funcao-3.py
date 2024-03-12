import cowsay
import random


def console_divertido(texto):
    funcoes = [
        cowsay.cow,
        cowsay.dragon,
        cowsay.turtle,
        cowsay.tux,
    ]

    funcao = random.choice(funcoes)
    funcao(texto)


console_divertido("Olá python!!!")
