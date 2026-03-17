"""Módulo para conversión de tipos de variables."""

# Conversion de tipos de variables
NUMERO_A_CONVERTIR = "5.8"
numero_a_float = float(NUMERO_A_CONVERTIR)
# OJO: Puedes pasar un string decimal a float, pero no directamente a int
NUMERO_A_INT = int(numero_a_float)
NUM_A_STRING = str(NUMERO_A_INT) + " y " + str(numero_a_float)

# OJO: La sentencia type() devuelve un objeto, por lo que hay que pasarlo a str
print(
    "El tipo de dato de numeroAConvertir ("
    + NUMERO_A_CONVERTIR
    + ") es: "
    + str(type(NUMERO_A_CONVERTIR))
)
print(
    "El tipo de dato de numeroAInt ("
    + str(NUMERO_A_INT)
    + ") es: "
    + str(type(NUMERO_A_INT))
)
print(
    "El tipo de dato de numeroAFloat ("
    + str(numero_a_float)
    + ") es: "
    + str(type(numero_a_float)),
)
print(
    "El tipo de dato de numeroConvertidoAString ("
    + NUM_A_STRING
    + ") es: "
    + str(type(NUM_A_STRING))
)

# EJEMPLO PRACTICO
# OJO: Los inputs solo trabajan con strings
edad = input("¿Cual es tu edad?: ")
print(type(edad))

edad_a_int = int(edad)
print(type(edad_a_int))

print("Tu edad en int es: ", edad_a_int)
