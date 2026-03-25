## Classes ##
class MyEmptyPerson:
    pass  ## Es simbólico, no hace nada


print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname, alias="sin alias"):  ## Constructor de clases
        """El self es de uso obligatorio, se refiere a el mismo
        Es como si en java hacemos un
        this.name = name;
        this.surname = surname;"""

        self.__name = name  # Propiedad privada __propiedad
        self.__surname = surname  # Propiedad privada __propiedad
        self.full_name = f"{name} {surname} [{alias}]"  ## Propiedad pública

    ## Get en cubierto
    def get_name(self):
        return self.__name

    ## Get en cubierto
    def get_surname(self):
        return self.__surname

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Antonio", "Hernández")
print(f"Mi nombre es {my_person.get_name()} y mi apellido es {my_person.get_surname()}")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Monkey D.", "Luffy")
my_other_person.full_name = "Monkey D. Luffy"
print(my_other_person.full_name)
