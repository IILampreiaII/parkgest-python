from .veiculo_model import Veiculo

class Parque:

    CAPACIDADE_MAXIMA = 30

    def __init__(self, veiculo):
        self._estadia_ativas= []
        self.veiculo = veiculo
    
    def estadias_ativas(self, veiculo):
        if not isinstance(veiculo, Veiculo):
            raise TypeError("É necessário um objeto veiculo")
        if veiculo in self._estadia_ativas:
            return False
        if self.vagas_disponiveis == 0:
            return False
        self._estadia_ativas.append(veiculo)
        return True

    @property
    def vagas_disponiveis(self):            
            return self.CAPACIDADE_MAXIMA - len(self._estadia_ativas)

    def apresentar(self):
        return (
            f"Capacidade: {self.CAPACIDADE_MAXIMA} | "
            f"Veiculo: {self.veiculo.apresentar()} | "
            f"Vagas disponiveis: {self.vagas_disponiveis}"
        )
