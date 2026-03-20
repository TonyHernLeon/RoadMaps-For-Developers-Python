## Listas ##
mi_lista = list()
mi_otra_lista = []

print(len(mi_lista))

mi_lista = [34, 62, 30, 30, 53, 17]

print(mi_lista)
print(len(mi_lista))

mi_otra_lista = [34, 1.74, "Antonio", "Hernandez"]
print(type(mi_lista))
print(type(mi_otra_lista), "\n")

print(mi_otra_lista[0])
print(mi_otra_lista[1])
print(mi_otra_lista[-1])
print(mi_otra_lista[-4])
## print(mi_otra_lista[-5]) ## Nos pasamos de index

## Estás dos formas es complicarse mucho la vida. NO USAR!!! ##
edad, altura, nombre, apellido = (
    mi_otra_lista  ## Mismo elementos que elementos de la lista
)
print("\n", nombre)

edad, altura, nombre, apellido = (
    mi_otra_lista[2],
    mi_otra_lista[1],
    mi_otra_lista[0],
    mi_otra_lista[3],
)
print("\n")
print(nombre)
print(edad, "\n")

## =================== ##

print(mi_lista + mi_otra_lista, "\n")


## Funciones de Sistema ##
## Insertar datos ##
mi_otra_lista.append("Macbook")
print(mi_otra_lista, "\n")

## Insertar datos en una posición concreta ##
mi_otra_lista.insert(2, "D.")
print(mi_otra_lista)

## Eliminar indicando datos ##
mi_lista.remove(30)
print(mi_lista)

## Eliminando un elemento ##
mi_lista.pop()  ## Devuelve el valor que hemos quitado en la lista
print(mi_lista)

## Eliminando un elemento por indice ##
del mi_lista[2]
print(mi_lista)

## Eliminar la lista completa ##
mi_lista.clear()
print(mi_lista, "\n")

## Copiar listas ##
mi_nueva_lista = mi_otra_lista.copy()
print(mi_nueva_lista)

## Revertir el orden en la lista ##
mi_nueva_lista.reverse()
print(mi_nueva_lista)

## Ordenar lista ##
mi_nueva_lista.sort()  ## Solo para valores 'int', no 'float' o 'str'
print(mi_nueva_lista)
