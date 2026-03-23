## Sets ##

## Creando Sets ##
mi_set = set()
mi_otra_set = {}

print(type(mi_set))
print(type(mi_otra_set))  ## Hasta aquí sería un dic por el tipádo dinámico

## Creamos listas y tuplas para ver diferencias
mi_lista = list()
mi_tupla = tuple()

mi_lista = [2, 5, 4, 2, 1, 5]  ## Lista con corchetes
mi_tupla = (2, 5, 4, 2, 1, 5)  ## Tupla con parantesis
mi_set = {2, 5, 4, 2, 1, 5}  ## Set con llaves

mi_otra_set = {"Antonio", "Hernandez", 34}

print(type(mi_otra_set))  ## Aquí ya tendríamos un Set
mi_otra_set = {30, 20, 10}  ## Valores duplicados solo contempla uno
print(len(mi_otra_set))

print("Mi lista: ", (mi_lista))
print("Mi tupla: ", (mi_tupla))
print("Mi set: ", (mi_set))

mi_lista.append(19)
## Las tuplas son inmutables, por lo que no se puede añadir ningún valor
mi_set.add(19)

print("Mi lista: ", (mi_lista))
print("Mi tupla: ", (mi_tupla))
print("Mi set: ", (mi_set))

mi_set.add(19)
print("Mi set: ", (mi_set))  ## No admite repetidos

print(19 in mi_set)
print(15 in mi_set)

mi_set.remove(19)
print(mi_set)

mi_set.clear()
print(mi_set)

del mi_set  ## A partir de aquí no existe el objeto mi_set
## print(mi_set) ## Borra completamente el objeto || NameError: name 'mi_set' is not defined

mi_set = {"Antonio", "Hernandez", 34}
print(mi_set)
mi_lista = list(mi_set)
print(mi_lista)

mi_otra_set = {"Java", "Python", "Angular"}
mi_nuevo_set = mi_set.union(mi_otra_set)
print(mi_nuevo_set.union(mi_nuevo_set))  ## No pasa nada porque no se admiten repetidos
print(mi_nuevo_set.union({"JavaScript", "C"}))

print(mi_nuevo_set.difference(mi_set))
