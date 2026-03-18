"""
Módulo de Sets
"""

# Variables
mi_set = set({1, 2, 3, 4, (2, 1, 3), 1, 1, 2, 1})
print(type(mi_set))
print(mi_set)

print(2 in mi_set)

## Propiedad union(), para anidar sets
set_1 = {1, 2, 3}
set_2 = {3, 2, 4}
set_3 = set_1.union(set_2)

print(set_3)

## Propiedad add(), para agregar elementos,
# siempre que el elemento no esté en el set ya
set_1.add(7)
print(set_1)

## Propiedad remove(), para eliminar elementos
set_1.remove(7)
print(set_1)

## Propiedad discard(), como remove pero
# si no existe este elemento, pasa
set_1.discard(6)
print(set_1)
