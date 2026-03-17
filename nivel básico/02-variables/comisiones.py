"""
Programa de ingresos:
Este programa consiste en simular un programa de calculo de ingresos, con comisiones
por venta. El usuario debe ingresas, nombre y número de ventas, y el programa
debe tomar esos datos y imprimir por pantalla los ingresos de su ventas, con
una comisión del 13%.
"""

NOMBRE_USER = input("¿Cuál es tu nombre?: ")
VENTAS_USER = input("¿Cuánto has vendido?: ")

VENTAS_CON_COMISION = round(float(VENTAS_USER) + (float(VENTAS_USER) * 0.13), 2)

print(f"{NOMBRE_USER} has vendido: {VENTAS_CON_COMISION}€ (Comisión del 13% incluida)")
