from flask import Flask , jsonify , request 
from src.base_dados import criar_tabela, adicionar_veiculo , listar_veiculos
from src.modelo.veiculo_model import Veiculo

app = Flask(__name__)

@app.get("/")
def inicio():
    return "Bem-vindo ParkGest!"

criar_tabela()

@app.get("/veiculo")
def obter_veiculos():
    dados = [f.para_dicionario() for f in listar_veiculos ()]
    return jsonify(dados)
 
@app.post("/veiculos")
def criar_veiculo():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify({"erro": "JSON inválido"}), 400
 
    try:
        f = Veiculo.de_dicionario(dados)
        adicionar_veiculo(f)
 
    except (KeyError, TypeError, ValueError):
        return jsonify({"erro": "Dados inválidos"}), 400
    return jsonify(f.para_dicionario()), 201