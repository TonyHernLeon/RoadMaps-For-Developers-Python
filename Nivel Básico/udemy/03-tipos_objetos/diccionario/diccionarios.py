"""
Módulo de Diccionarios
"""

# Variables
diccionario = {"key1": "valor1", "key2": "valor2"}

print(type(diccionario))
print(diccionario)

valor_diccionario_key1 = diccionario["key1"]
print(valor_diccionario_key1)

## Ejemplo diccionario cliente

cliente = {"nombre": "Antonio", "apellido": "Hernandez", "peso": 90, "altura": 1.74}
consulta_apellido = cliente["apellido"]
print(consulta_apellido)

## Diccionario con diferentes valores
dic_variado = {"key1": 55, "key2": [10, 20, 30], "key3": {"key1": 100, "key2": 200}}

print(dic_variado["key1"])
print(dic_variado["key2"])
print(dic_variado["key3"])

## Tarea. Tenemos un diccionario, y tenemos que coger un valor y ponerlo en mayusculas
dic_tarea = {"key1": ["a", "b", "c"], "key2": ["d", "e", "f"]}
valor_upper = dic_tarea["key2"][1].upper()

print(valor_upper)

## Agregar elementos al diccionario
diccionario_add = {"key1": "a", "key2": "b"}

print(diccionario_add)
diccionario_add[3] = "c"
print(diccionario_add)

## También se cambia el valor
diccionario_add["key2"] = "B"
print(diccionario_add)

## Obtener todas las keys
print(diccionario.keys())

## Obtener todas las values
print(diccionario.values())

## Obtener todas las elementos
print(diccionario.items())
