import sqlite3
from contextlib import closing
from src.modelo.veiculo_model import Veiculo
 
def criar_tabela(caminho="parkgest.db"):
    with closing(sqlite3.connect(caminho)) as ligacao:
        with ligacao:
            ligacao.execute("""
                CREATE TABLE IF NOT EXISTS veiculos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    matricula TEXT NOT NULL UNIQUE,
                )
            """)

def adicionar_veiculo(objeto, caminho="parkgest.db"):
    dados = objeto.para_dicionario()
 
    with closing(sqlite3.connect(caminho)) as ligacao:
        with ligacao:
            ligacao.execute(
                "INSERT INTO veiculos (id, matricula) VALUES (?, ?)",
                (dados["id"], dados["matricula"])
            )

def listar_veiculos(caminho="parkgest.db"):
    with closing(sqlite3.connect(caminho)) as ligacao:
        linhas = ligacao.execute(
            "SELECT id, matricula FROM veiculos"
        ).fetchall()
 
    return [Veiculo(id, matricula) for id, matricula in linhas]