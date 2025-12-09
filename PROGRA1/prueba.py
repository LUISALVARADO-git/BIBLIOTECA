class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

c = Cuenta(100)
print("Saldo inicial:", c.get_saldo())

try:
    x = int(input("Edad: "))
    y = 10 / x
    print("Resultado:", y)
except ValueError:
    print("Error: Debes ingresar un número entero válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

print("Listo")