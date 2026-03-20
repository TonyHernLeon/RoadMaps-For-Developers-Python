## Strings ##
mi_string = "Mi String"
mi_otro_string = "Mi otro String"

print(len(mi_string))
print(len(mi_otro_string))

print(mi_string, mi_otro_string)
print(mi_string + " " + mi_otro_string)

mi_string_con_salto = "Mi String \ncon salto de linea"
print(mi_string_con_salto)

mi_string_tab = "Mi String con \ttabulación"
print(mi_string_tab)

mi_string_escapado = "\tMi String es un String \nescapado"  ## Con doble barra se anula
print(mi_string_escapado)


## Formateo ##
name, surname, age = "Antonio", "Hernandez", 34
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))

## Inferencia de datos ##
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

## Desempaquetado de caracteres ##
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(f)
print(e)

## División ##
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

## Reverse ##
reversed_language = language[::-1]
print(reversed_language)

language_slice = language[0::3]
print(language_slice)

## Funciones de Sistema
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("2".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("Py"))
print("Py" == "py")
