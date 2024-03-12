ano_nascimento = int(input("Em que ano você nasceu? "))

if ano_nascimento >= 1946 and ano_nascimento <= 1964:
    geracao = "Baby Boomer"
elif ano_nascimento >= 1965 and ano_nascimento <= 1980:
    geracao = "Geração X"
elif ano_nascimento >= 1981 and ano_nascimento <= 1996:
    geracao = "Millenial"
elif ano_nascimento >= 1997:
    geracao = "Geração Alpha"
else:
    geracao = "Não encontrada"

print(geracao)
