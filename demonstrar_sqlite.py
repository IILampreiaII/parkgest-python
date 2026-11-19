from src.modelo.veiculo_model import Veiculo
from src.base_dados import (criar_tabela, adicionar_veiculo, listar_veiculos)

def demonstrar():
    criar_tabela()
    adicionar_veiculo(Veiculo(1, "AA-11-BB"))
    adicionar_veiculo(Veiculo(2, "CC-22-DD"))

    for veiculo in listar_veiculos():
        print(veiculo.apresentar())
 
if __name__ == "__main__":
    demonstrar()