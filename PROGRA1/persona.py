class DatoInvalidoError(Exception):
    pass

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        if edad < 0:
            raise DatoInvalidoError("La edad no puede ser negativa")
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise DatoInvalidoError("La edad no puede ser negativa")
        self.__edad = valor

    def __repr__(self):
        return f"Persona(nombre='{self.__nombre}', edad={self.__edad})"
