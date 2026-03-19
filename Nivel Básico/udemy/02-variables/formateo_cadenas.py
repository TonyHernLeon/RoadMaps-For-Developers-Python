"""Módulo de Formateo de Cadenas"""

# Constantes
MATRICULA_COCHE = "1234ABC"
COLOR_COCHE = "AZUL FLORIDA"
NUM_PUERTAS = 5

# Función .format || OJO: Sirve para todo tipo de variables
print(
    "El coches es {}, tiene {} puertas y su matricula es {}".format(
        COLOR_COCHE, NUM_PUERTAS, MATRICULA_COCHE
    )
)

# Cadenas literales || OJO: Solo sirve para tipo de variables != String
print(
    f"El coches es {COLOR_COCHE}, tiene {NUM_PUERTAS} puertas y "
    + "su matrícula es "
    + MATRICULA_COCHE
)
