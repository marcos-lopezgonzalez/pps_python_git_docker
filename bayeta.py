from pymongo import MongoClient
from prueba_mongo import consultar


def frotar(n_frases: int = 1) -> list:
    frases = consultar(n_frases)
    lista_de_frases = [frase['frase'] for frase in frases]
    return lista_de_frases
