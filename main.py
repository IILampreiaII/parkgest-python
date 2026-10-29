import json
from pathlib import Path
from src.modelo import Parque, Veiculo

veiculo1 = Veiculo("HB-09-JK")
print(veiculo1.apresentar())
veiculo2 = Veiculo("KJ-23-LT")
print(veiculo2.apresentar())
veiculo3 = Veiculo("TB-82-VS")
print(veiculo3.apresentar())
veiculo4 = Veiculo("FJ-74-IA")
print(veiculo4.apresentar())

parque1 = Parque(veiculo1)
print(parque1.estadias_ativas(veiculo1))
print(parque1.vagas_disponiveis)
print(parque1.apresentar())


