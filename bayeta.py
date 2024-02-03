from pymongo import MongoClient
from prueba_mongo import consultar, insertar_frases


def frotar(n_frases: int = 1) -> list:
    frases = consultar(n_frases)
    lista_de_frases = [frase['frase'] for frase in frases]
    return lista_de_frases

def nuevas_frases(lista_frases: list):
    status_insercion = insertar_frases(lista_frases)
    return status_insercion
