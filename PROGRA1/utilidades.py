import random


def es_password_segura(clave: str) -> bool:
    if len(clave)<8:
        return False
    return True

def nombre_aleatorio()-> str:
    nombres=["LUIS", "SINATRA", "ELIAS", "MARIA"]
    return random.choice(nombres)

def porcentaje(parte, total) -> float:
    if total <= 0:
        raise ValueError("El total debe ser mayor que cero")
    return (parte / total) * 100


