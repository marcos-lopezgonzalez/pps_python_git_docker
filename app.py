from bayeta import frotar
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Hola, mundo"

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def get_frotar(n_frases):
    frases = frotar(n_frases)
    return jsonify({"frases": frases})

if __name__ == '__main__':
    app.run()
