## Operadores Aritméticos ##
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(4 % 2)
print(10 // 2)
print(10**2)
print(10**2 + 2 - 4 // 6 % 3)

print("Hola" + "Python" + "Que tal¿?")
print("Hola" + str(59))
print("Hola " * 5)
print("Hola " * (2**3))

my_float = 2.5 * 2
print("Hola " * int(my_float) + "\n")

## Operadores Comparativos ##
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)

## Compara ordenación alfabética ASCII
print("Comparación de 'Hola' < 'Python':", "Hola" < "Python")
print("Comparación de 'Hola' > 'Python':", "Hola" > "Python")
print("Comparación de 'Hola' >= 'Python':", "Hola" >= "Python")
print("Comparación de 'Hola' <= 'Python':", "Hola" <= "Python")
print("Comparación de 'Hola' == 'Python':", "Hola" == "Python")
print("Comparación de 'Hola' != 'Python':", "Hola" != "Python")

print("Comparación de 'Hola' != 'Zola':", "Hola" >= "Zola")
print("Comparación de 'Hola' != 'Bola':", "Hola" >= "Bola")

## Cuenta Caractéres
print(
    "Comparación de cantidad de caracteres 'Hola' == 'Bola':",
    len("Hola") >= len("Bola"),
)
print("\n")

## Operadores Lógicos ##
print(3 > 4 and "Hola" > "Python")
print(3 > 4 and "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(not (3 > 4))
