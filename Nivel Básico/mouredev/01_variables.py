# Variables
"""Aunque Python es muy flexible a la hora de
crear variables. Es verdad, que las formas válidas son:
· Snake Case => snake_case.
· CamelCase => camelCase
· excepsiones => _if. Solo para usar en con palabras reservadas. Poco usadas."""

## Variables
my_string_variable = "Mi Variable String"
print(my_string_variable)
my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable, type(my_int_to_str_variable))

## Variables en una sola linea. || Cuidado con abusar con esta sintaxis!!
name, surname, alias, age = "Antonio", "Hernandez", "Tony_HernLeon", 34
print("Soy", surname, name, "\nMi alias es:", alias, "\nMi edad es:", age, "\n")

## Concatenación de variables en un print
print(
    my_string_variable,
    my_int_variable,
    my_int_to_str_variable,
    my_bool_variable,
)
print("Este es el valor de:", my_bool_variable)

## Algunas funciones de Sistema
print(len(my_string_variable))

## Inputs
"""first_name = input("Cual es tu nombre?: ")
age = input("Que edad tienes:¿? ")

print(first_name)
print(age)"""


## ¿Forzamos el tipado de la variable?
mi_variable_str: str = "Mi variable"
mi_variable_str = 32
print(mi_variable_str)
print(type(mi_variable_str))
