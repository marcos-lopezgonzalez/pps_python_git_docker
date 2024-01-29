import random

def frotar(n_frases: int = 1) -> list:
    with open('frases.txt', 'r', encoding='utf-8') as file:
        lista_de_frases = [line.strip() for line in file]

    frases_elegidas = random.sample(lista_de_frases, min(n_frases, len(lista_de_frases)))

    return frases_elegidas

