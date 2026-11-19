from src.entradas import resumo_entrada

class Veiculo:

    def __init__(self, matricula_valida: str):
        self.matricula_valida = matricula_valida

    @property
    def matricula_valida(self):
        return self._matricula_valida

    @matricula_valida.setter
    def matricula_valida(self, valor):
        if not resumo_entrada(valor,str) or not valor.strip():
            raise ValueError("Matricula não e válida")
        self._matricula_valida = valor.strip()

    def apresentar(self):
        return f"matricula: {self.matricula_valida}"

    @classmethod
    def de_dicionario(cls, dados):
        return cls(dados["matricula_valida"])

    #dicionario de serializacao 
    def para_dicionario(self):
          return { 
                "matricula_valida":self.matricula_valida
        }

