def calcular_media_simples(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def calcular_media_ponterada(n1, n2, n3):
    return (n1 * 2 + n2 * 3 + n3 * 5) / 10


def melhor_media(n1, n2, n3):
    med1 = calcular_media_simples(n1, n2, n3)
    med2 = calcular_media_ponterada(n1, n2, n3)

    return med1 if med1 > med2 else med2


resultado1 = melhor_media(5, 6, 9)
resultado2 = melhor_media(9, 6, 5)

print(resultado1)
print(resultado2)
