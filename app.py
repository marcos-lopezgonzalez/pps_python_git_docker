from bayeta import frotar, nuevas_frases
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Hola, mundo"

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def get_frotar(n_frases):
    frases = frotar(n_frases)
    return jsonify({"frases": frases})

@app.route('/frotar/add', methods=['POST'])
def add_frotar():
    datos_json = request.get_json()
    frases = datos_json.get('frases', [])

    if not isinstance(frases, list):
        return jsonify({"error": "El formato debe ser una lista"}), 400

    status_solicitud = nuevas_frases(frases)

    if status_solicitud:
        return jsonify({"mensaje": "Frases añadidas correctamente"}), 200
    else:
        return jsonify({"error": "Error al añadir frases"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
