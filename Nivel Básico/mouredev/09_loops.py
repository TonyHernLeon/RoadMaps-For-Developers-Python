## Loops ##

### While ###
mi_condicion = 0
while mi_condicion < 10:
    print("\t", mi_condicion)
    mi_condicion += 1
else:  ## Es opcional
    print("\tMi condición es mayor o igual que 10")

print("La ejecución continua")
print("|=============================|")

mi_condicion = 0
while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 15:
        print("Mi condición es 15")
        print("Se detiene la ejecución")
        break

    print("\t", mi_condicion)

print("La ejecución continua\n\t |######## FIN DE WHILE ########|")

## For ##
print("##### LISTA FOR #####")
mi_lista = [35, 24, 57, 89, 45, 13]
for element in mi_lista:
    print(element)

mi_tupla = (34, 1.74, "Antonio", "Hernandez", " ")
for element in mi_tupla:
    print(element)

print("\n##### SET FOR #####")
mi_otra_set = {"Antonio", "Hernandez", 34}
for element in mi_otra_set:
    print(element)

print("\n##### DICCIONARIO FOR #####")
mi_otro_dict = {
    "Nombre": "Antonio",
    "Apellido": "Hernandez",
    "Edad": 34,
    1: "Python",
}
for element in mi_otro_dict:
    print(element)  ## De aquí solo saldría las keys
    ## for value in mi_otro_dict.values():
    ##     print(value)  ## Si se quiere los valores
    if element == "Edad":
        ## continue ## Para seguir con el bucle
        break  ## Para romper el for, saltaría el else también
else:  ## Cuando termine el for
    print("El bucle For apra mi diccionario ha finalizado")
