"""Programa de ingresos"""

NOMBRE_USER = input("¿Cuál es tu nombre?: ")
VENTAS_USER = input("¿Cuánto has vendido?: ")

VENTAS_CON_COMISION = round(float(VENTAS_USER) + (float(VENTAS_USER) * 0.13), 2)

print(f"{NOMBRE_USER} has vendido: {VENTAS_CON_COMISION}€ (Comisión del 13% incluida)")
