# API - é um lugar para disponibilizar recurso e/ou funcionalidades

# 1. Objetivo - Criar api que disponibiliza consulta, criação, edição e exclusão de carros
# 2. URL base - localhost
# 3. Endpoints
    #localhost/livros(GET)
    #localhost/livros/id(GET)
    #localhost/livros/id(PUT)
    #localhost/livros/id(DELETE)
# 4. Quais recursos - carros

from flask import Flask, jsonify, request
app = Flask(__name__)
carros = [
    {
        'id': 1,
        'nome': 'Toyota Hilux',
        'categoria': 'camionete',
        'ano': 2020
    },

    {
        'id': 2,
        'nome': 'Mitsubish S10',
        'categoria': 'camionete',
        'ano': 2022
    },

    {
        'id': 3,
        'nome': 'Ford Ranger',
        'categoria': 'camionete',
        'ano': 2023
    },

    {
        'id': 4,
        'nome': 'Nissan Frontier',
        'categoria': 'camionete',
        'ano': 2019
    },

    {
        'id': 5,
        'nome': 'Wolksvagen Amarok',
        'categoria': 'camionete',
        'ano': 2021
    },
]

#consultar todos
@app.route('/carros',methods=['GET'])
def consultar_carros():
    return jsonify(carros)

#consultar por ID
@app.route('/carros/<int:id>', methods=['GET'])
def consultar_carros_id(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(carro)
#editar
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            carros[indice].update(carro_alterado)
            return jsonify(carros[indice])
#adicionar
@app.route('/carros', methods=['POST'])
def adicionar_carro():
    novo_carro = request.get_json()
    carros.append(novo_carro)
    return jsonify(carros)
#excluir
@app.route('/carros/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            del carros[indice]
    return jsonify(carros)

app.run(port=5000, host='localhost', debug=True)