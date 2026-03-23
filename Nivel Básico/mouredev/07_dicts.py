## Diccionarios ##
mi_dict = dict()
mi_otro_dict = {}

print(type(mi_dict))
print(type(mi_otro_dict))

mi_otro_dict = {
    "Nombre": "Antonio",
    "Apellido": "Hernandez",
    "Edad": 34,
    1: "Python",
}  ## relación Clave:Valor

mi_dict = {
    "Nombre": "Antonio",
    "Apellido": "Hernandez",
    "Edad": 34,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
}

print(mi_otro_dict)
print(mi_dict)

print(mi_dict["Nombre"])

mi_dict["Direccion"] = "Playa de Rota"
print(mi_dict)

del mi_dict["Direccion"]  ## Así eliminamos un elemento indicado
print(mi_dict)

print("Antonio" in mi_dict)
print("Nombre" in mi_dict)  ## Se busca por clave, no por valor

print(mi_dict.items())
print(mi_dict.keys())
print(mi_dict.values())
## print(mi_dict.fromkeys()) TypeError: fromkeys expected at least 1 argument, got 0

mi_nuevo_dict = mi_dict.fromkeys(
    "Nombre", 1
)  ## Crea un diccionario nuevo, como valor 1 en todas las keys
print(mi_nuevo_dict)

mi_nuevo_dict = dict.fromkeys(
    mi_dict
)  ## Crea un diccionario nuevo, con la estructura de mi_dict, sin valores
print(mi_nuevo_dict)

mis_valores = mi_nuevo_dict.values()
print(type(mis_valores))

print(type(mi_nuevo_dict.values()))
print(list(dict.fromkeys(list(mi_nuevo_dict.values()))))
print(tuple(mi_nuevo_dict))
print(set(mi_nuevo_dict))
