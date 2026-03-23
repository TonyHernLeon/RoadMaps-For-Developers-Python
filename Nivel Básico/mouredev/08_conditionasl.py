## Condicionales ##
mi_condicion = True

if mi_condicion:  ## Es lo mismo que if mi_condicion == True
    print("Se ejecuta la condicion del if")

    mi_condicion = 5 * 3
    if mi_condicion > 10 and mi_condicion < 20:
        print("\tEs mayor que 10 y menor que 20")

    elif mi_condicion == 25:
        print("\tIgual que 25")
    else:
        print("\tEs distinto de 25")

print(
    "Es menor que 10"
)  ## Hay que tener en cuenta las tabs en Python, porque se ejecuta siempre
print("La ejecución continúa")

mi_string = "Mi cadena de texto"

if mi_string:
    print("\tMi cadena de texto no está vacía")

if mi_string == "Mi cadena de texto":
    print("\tEstas cadenas de texto coinciden.")
