from flask import Flask, jsonify, request

app = Flask(__name__)

dados = [
    {
        "id": 0,
        "umidade": 0,
        "chuva": 0,
        "celsius": 0,
        "fahrenheit": 33.8,
        "kelvin": 272,
        "data": '0000-00-00',
        "hora": '00:00:00',
    }
]


# Consultar(todos)
@app.route('/clima/', methods=['GET'])
def obter_clima():
    return jsonify(dados)


# Consultar por id
@app.route('/clima/<int:id>', methods=['GET'])
def detalhes_clima(id):
    for clima in dados:
        if clima.get('id') == id:
            return jsonify(clima)


# Consultar Ultimo Cliente
@app.route('/', methods=['GET'])
def ultimo_clima():
    id = dados[-1]['id']
    for clima in dados:
        if clima.get('id') == id:
            return jsonify(clima)


# Editar
@app.route('/clima/<int:id>', methods=['PUT'])
def atualizar_clima(id):
    clima_alterado = request.get_json()
    for indice, clima in enumerate(dados):
        if clima.get('id') == id:
            dados[indice].update(clima_alterado)
            return jsonify(dados[indice])


# Criar
@app.route('/clima/', methods=['POST'])
def criar_clima():
    novo_clima = request.get_json()
    dados.append(novo_clima)
    return jsonify(dados)


# Criar id Incremental
@app.route('/clima/id/', methods=['POST'])
def criar_clima_id():
    novo_clima = {
        'id': dados[-1]['id'] + 1,
        'umidade': request.json.get('umidade', ""),
        'chuva': request.json.get('chuva', ""),
        'celsius': request.json.get('celsius', ""),
        'fahrenheit': request.json.get('fahrenheit', ""),
        'kelvin': request.json.get('kelvin', ""),
        'data': request.json.get('data', ""),
        'hora': request.json.get('hora', "")
    }
    dados.append(novo_clima)
    return jsonify(dados)


# Excluir por id
@app.route('/clima/<int:id>', methods=['DELETE'])
def deletar_clima(id):
    for indice, clima in enumerate(dados):
        if clima.get('id') == id:
            del dados[indice]
    return jsonify(dados)



app.run(port=5000, host='localhost', debug=True)
