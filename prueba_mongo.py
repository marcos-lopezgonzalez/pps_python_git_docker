from pymongo import MongoClient

# Conexión con el motor de Mongo
cliente_mongo = MongoClient('mongodb://mongo_db:27017/')

def instanciar():
    # Conexión con la BD (la crea si no existe)
    coleccion = cliente_mongo['bayeta']
    # Conexión con la tabla (llamada colección en Mongo)
    return coleccion['frases_auspiciosas']

def cerrar_conexion():
    # Ceramos la conexión
    cliente_mongo.close()

def inicializar_coleccion(coleccion):
    # Insertar datos iniciales (usando el archivo de texto)
    with open('frases.txt', 'r', encoding='utf-8') as file:
        frases = [{"frase": line.strip()} for line in file]
    coleccion.insert_many(frases)

def borrar_coleccion(coleccion):
    # Borramos el contenido de la colección
    coleccion.delete_many({})

def consultar(n_frases: int = 1):
    coleccion = instanciar()
    # Comprobamos si la colección está vacía
    if coleccion.count_documents({}) == 0:
        inicializar_coleccion(coleccion)
    # Obtenemos una cantidad n_frases de frases
    frases = coleccion.aggregate([{'$sample': {'size': n_frases}}])
    # No es necesario cerrar la conexión, ya que cuando se pare el contenedor esto se hará automáticamente.
    #cerrar_conexion()
    return list(frases)
