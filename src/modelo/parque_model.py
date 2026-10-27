class Parque:

    CAPACIDADE_MAXIMA = 30

    def __init__(self, capacidade):
        self._veiculos_presentes = []
       
    @property
    def vagas_disponiveis(self):
        return self.CAPACIDADE_MAXIMA - len(self._presentes)

    def aprensentar(self):
        return (
            f"Veiculos presentes: {self._presentes}"
            f"Capacidade:{self.CAPACIDADE_MAXIMA}"
            f"Vagas disponiveis: {self.vagas_disponiveis}"
        )
