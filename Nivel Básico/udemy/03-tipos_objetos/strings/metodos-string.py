"""
Módulo de métodos de String
"""

# Constante
TEXTO = "Este es el texto de Antonio"

## Método UPPER (pasamos a mayusuculas todo el texto)
texto_mayusculas = TEXTO.upper()
print(texto_mayusculas)

sub_texto_mayusculas = TEXTO[4:9].upper()
print(sub_texto_mayusculas)

## Split (separa por espacios vacíos, por defecto)
texto_separado = TEXTO.split()
print(texto_separado)

texto_separado_por_t = TEXTO.split("t")
print(texto_separado_por_t)

## Join (Para unir cadenas)
a = "Aprender"
b = "Python"
c = "Mola"
e = " ".join([a, b, c])
print(e)

## Find (para encontrar un caracter, devuelve un -1 si no encuentra nada)
resultado_find = TEXTO.find("z")
print(resultado_find)

## Replace. Para reemplazar cadenas

resultado_replace = TEXTO.replace("Antonio", "Todos")
print(resultado_replace)
