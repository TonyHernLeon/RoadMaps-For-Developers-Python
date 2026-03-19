"""
Módulo de Tarea.

La tarea consiste es pedirle al usuario que introduzco un texto, y una vez introducido
le pedirá al usuario que introduzca tres letras a su elección.

Con estas letras tendremos que:
· Contar las veces que salen esas letras.
· Contar todas las palabras que hay en el texto
· Cual es la primera y última letra del texto
· Invertir el orden del texto
· Si aparece en el texto la palabra 'Python'
"""

# Solicitamos al usuario el texto
texto_a_analizar = input("Introduzca un texto, poema, frase... a analizar:   ")

# Le pedimos al usuario que introduzca tres letras
lista_letras = list()
lista_letras.append(
    input("Necesito que introduzca tres letras para analizar el texto.\nLetra 1: ")
)
lista_letras.append(input("Letra 2: "))
lista_letras.append(input("Letra 3: "))

# Pasamos el texto y letras a minusculas para que todo sea igual
texto_minuscula = texto_a_analizar.lower()
letra_3_minuscula = lista_letras[2].lower()

print(
    f"La letra {lista_letras[0]} aparece {texto_minuscula.count(lista_letras[0].lower())} veces"
)
print(
    f"La letra {lista_letras[1]} aparece {texto_minuscula.count(lista_letras[1].lower())} veces"
)
print(
    f"La letra {lista_letras[2]} aparece {texto_minuscula.count(lista_letras[2])} veces"
)

## Contamos todas las palabras
lista_palabras = texto_a_analizar.split()
print(f"El texto escrito tiene {len(lista_palabras)} palabras")

# Comprobar cual es la primera letra y la última
primera_letra = texto_a_analizar[0]
texto_invertido = texto_a_analizar[::-1]

print(f"La primera letra del texto es la: {primera_letra}")
print(f"La última letra del texto es la: {texto_invertido[0]}")
print(f"El texto invertido es: {texto_invertido}")

palabra_python = "Python"
tiene_palabra = texto_minuscula.find(palabra_python.lower()) != -1

print(f"Aparece la palabra 'Python'¿?: {tiene_palabra}")
