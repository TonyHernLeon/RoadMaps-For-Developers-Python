"""
Módulo de Tuples
"""

## inicialización variables
mi_tuple = (1, 2, 3, 4)
t = (5, 5.6, "ff")  ## Se puede mezclar
print(f"Tipo de mi_tuple: {type(mi_tuple)}")
print(mi_tuple[0])

## Los tuples son inmutables, pero se pueden anidar y demás
nuevo_tuple = (1, 2, (10, 20), 4)
print(type(nuevo_tuple))
nuevo_tuple = list(nuevo_tuple)
print(type(nuevo_tuple))

## Desfragmentar tuples. Se debe tener los mismo elementos
tupl = (1, 2, 3)
x, y, z = tupl
print(x, y, z)
