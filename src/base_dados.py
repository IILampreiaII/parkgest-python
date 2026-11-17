
import sqlite3
from contextlib import closing
from pathlib import Path


def criar_tabela(caminho):
    """Cria a tabela de veículos."""

    Path(caminho).parent.mkdir(parents=True, exist_ok=True)

    with closing(sqlite3.connect(caminho)) as ligacao:
        with ligacao:
            ligacao.execute("""
                CREATE TABLE IF NOT EXISTS veiculos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    matricula TEXT NOT NULL UNIQUE
                )
            """)


def adicionar_veiculo(objeto, caminho):
    """Adiciona um veículo à base de dados."""

    with closing(sqlite3.connect(caminho)) as ligacao:
        try:
            with ligacao:
                ligacao.execute("""
                    INSERT INTO veiculos (matricula)
                    VALUES (?)
                """, (objeto.matricula_valida,))

            print(
                f"Veículo {objeto.matricula_valida} adicionado."
            )

        except sqlite3.IntegrityError:
            print(
                f"Veículo {objeto.matricula_valida} já existe."
            )


def listar_veiculos(caminho):
    """Lista todos os veículos registados."""

    with closing(sqlite3.connect(caminho)) as ligacao:
        cursor = ligacao.execute("""
            SELECT id, matricula
            FROM veiculos
            ORDER BY id
        """)

        return cursor.fetchall()
