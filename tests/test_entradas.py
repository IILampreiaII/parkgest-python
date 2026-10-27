import unittest
from src.modelo import Veiculo, Parque, Estadia

def pode_registar_entrada(veiculo_valido, vaga_disponivel):
    return veiculo_valido and vaga_disponivel

class TesteVaga(unittest.TestCase):

    def teste_permitir_entrada_veiculo_valido_com_vaga(self):
        self.assertTrue(
            pode_registar_entrada(True, True)
        )

    def teste_rejeitar_veiculo_invalido_com_vaga(self):
            self.assertFalse(
                pode_registar_entrada(False, True)
            )

    def teste_rejeitar_entrada_veiculo_valido_sem_vaga(self):
        self.assertFalse(
            pode_registar_entrada(True, False)
        )

    def teste_rejeitar_veiculo_invalido_sem_vaga(self):
        self.assertFalse(
            pode_registar_entrada(False, False)
            )