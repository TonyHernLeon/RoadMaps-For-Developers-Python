"""
Módulo de listas
"""

mi_lista = ["a", "b", "c"]

print(mi_lista)
print(type(mi_lista))

## Concatenar lista
contingua_lista = ["d", "e", "f"]

lista_completa = mi_lista + contingua_lista

print(lista_completa)

## Append, para agregar a la lista
lista_completa.append("g")
print(lista_completa)

## Pop, para eliminar de la lista (por defecto borra el último)
elemento_eliminado = lista_completa.pop()
print(elemento_eliminado)
print(lista_completa)

elemento_eliminado = lista_completa.pop(4)
print(elemento_eliminado)
print(lista_completa)

# Ordenar lista
lista_desordenada = [6, 5, 8, 3, 9, 7, 2, 1, 4]
## lista_ordenada = lista_desordenada.sort() esto no tiene sentido
lista_desordenada.sort()
print(lista_desordenada)

# Ordenar inverso
lista_desordenada.reverse()
print(lista_desordenada)  ## Como Sort no devuelve nada
