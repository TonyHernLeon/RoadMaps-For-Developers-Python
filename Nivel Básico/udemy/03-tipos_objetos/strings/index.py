"""
Módulo sobre indices de cadenas
"""

# Constantes
MI_CADENA = "cadena de prueba para index"

# ** Conocer que caracter hay en cada indice
caracter_por_indice = MI_CADENA[4]
print(f"El caracter en el indice 4 en MI_CADENA es: {caracter_por_indice}")

# Método Index() => Solo te da el primer caracter encontrado
# ** Conocer el indice de un caracter
caracter_por_index = MI_CADENA.index("de")
print(f"El caracter 'de' está en el indice {caracter_por_index} en MI_CADENA")
