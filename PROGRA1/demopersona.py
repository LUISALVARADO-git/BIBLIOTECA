from persona import Persona, DatoInvalidoError


persona1 = Persona("Ana", 25)
persona2 = Persona("Luis", 30)
print(persona1)
print(persona2)


try:
    persona3 = Persona("Carlos", -5)
except DatoInvalidoError as e:
    print("Error al crear persona:", e)


try:
    persona1.edad = -10
except DatoInvalidoError as e:
    print("Error al asignar edad:", e)
