## Tuplas. Conjunto de valores ##
## Diferencias en entre Listas y Tuplas, las Tuplas son inmutables ##
mi_tupla = tuple()
mi_otra_tupla = (30, 60, 70)

mi_tupla = (34, 1.74, "Antonio", "Hernandez", " ")
print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla[0])
print(mi_tupla[-1])

print(mi_tupla.count("Antonio"))
print(mi_tupla.index("Antonio"))
print(mi_tupla.index("Hernandez"))

## mi_tupla[1] = 1.80   ## TypeError: 'tuple' object does not support item assignment
print(mi_tupla + mi_otra_tupla)

mi_tupla_sumada = mi_tupla + mi_otra_tupla
print(mi_tupla_sumada)
print(mi_tupla_sumada[3:6])

mi_tupla = list(mi_tupla)
print(type(mi_tupla))

mi_tupla[4] = "Tony_HernLeon"
mi_tupla.insert(1, "Azul")
print(tuple(mi_tupla))

del mi_tupla
# print(mi_tupla) ## NameError: name 'mi_tupla' is not defined
