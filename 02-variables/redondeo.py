"""Modulo de redondeo de números"""

# Constantes
NUM = 2.5
NUM_1 = 4.2
NUM_2 = 5.6

# Redondeo - round(): Redondea hacia donde más cerca de
# la parte entera se encuentre el decimal
print(f"El redondeo de {NUM}, utilizando round() es {round(NUM)}")
print(f"El redondeo de {NUM_1}, utilizando round() es {round(NUM_1)}")
print(f"El redondeo de {NUM_2}, utilizando round() es {round(NUM_2)}")

RESULTADO = 90 / 7
redondeo = round(RESULTADO, 3)  ## NOTA: Indicamos el número de decimales
print(redondeo)
