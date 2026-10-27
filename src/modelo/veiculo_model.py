from src.entradas import matricula

class Veiculo:

    def __init__(self, matricula_valida: str):
        self.matricula = matricula_valida

    @property
    def matricula_valida(self):
        return self._matricula_valida

    @matricula_valida.setter
    def matricula_valida(self, valor):
        if not matricula(valor):
            raise ValueError("Matricula não e válida")
        self._matricula_valida = valor.strip()