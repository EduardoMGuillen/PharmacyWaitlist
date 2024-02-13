# Turnero Farmacia
# Perfumeria, farmacia, cosmetico
# Preguntar area y dar numero Generador
# Preguntar por otro turno
# Su turno es: - Aguarde y sera atendido Decorador
# Separar codigo Numero.py Generadores y decorador \ principal funciones programa

from Dia_8 import Numero


def inicio():
    print("Elige: Farmacia (F), Perfumeria (P), Cosmeticos (C)")
    opcion = input().upper()
    Numero.decorador(opcion)

run = True

while run:
    inicio()
