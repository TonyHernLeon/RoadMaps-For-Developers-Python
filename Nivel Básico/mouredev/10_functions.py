## Funciones ##
def mi_funcion():
    print("##### MI PRIMERA FUNCION #####")
    print("Esto es una función")


mi_funcion()


def sum_dos_valores(primer_valor: int, segundo_valor):
    print("##### FUNCION SUMA #####")
    print(primer_valor + segundo_valor)


sum_dos_valores(3, 2)
sum_dos_valores("3", "2")  ## Aquí lo que pasaría es que se concatenaría


def sum_dos_valores_with_return(primer_valor, segundo_valor):
    print("##### FUNCION SUMA CON RETURN #####")
    return primer_valor + segundo_valor


print(sum_dos_valores_with_return(10, 5))
print(
    sum_dos_valores_with_return("10", "5")
)  ## Concatena los parametros que son cadenas


def imprimir_nombre(nombre, apellido):
    print("##### FUNCION IMPRIMIR NOMBRE Y APELLIDO #####")
    print(f"{nombre} {apellido}")


imprimir_nombre(
    "Antonio", "Hernandez"
)  ## Puede provocar error a la hora de introducir los parametros
imprimir_nombre(apellido="Hernandez", nombre="Antonio")  ## De esta forma no pasaría


def imprimir_nombre_with_default(nombre, apellido, alias="Sin Alias"):
    print("##### FUNCION IMPRIMIR NOMBRE, APELLIDO Y ALIAS CON DEFAULT #####")
    print(f"{nombre} {apellido}, {alias}")


imprimir_nombre_with_default("Antonio", "Hernandez")


def imprimir_textos(*text):  ## Para infinitos parametros añadimos el *
    print(text)


imprimir_textos("hola", "Python", "Antonio", 34)
imprimir_textos("Python")


def imprimir_upper_textos(*texts):  ## Para infinitos parametros añadimos el *
    for text in texts:
        print(text.upper())


def suma_numeros_absolutos(*numeros_absoluto):
    total_suma = 0
    for numero in numeros_absoluto:
        ## La función de sistema abs(num), coge el valor
        ## absoluto del numero ya sea negativo o positivo
        total_suma += abs(numero)
    return f"La suma de números absolutos es: {total_suma}"
