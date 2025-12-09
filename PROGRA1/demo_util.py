import utilidades

#pass
print(utilidades.es_password_segura("12345sies"))   
print(utilidades.es_password_segura("321no"))       


#nombres
for _ in range(4):
    print("El nombre aleatorio:", utilidades.nombre_aleatorio())


#porcentaje
print(utilidades.porcentaje(50, 200))  
try:
    print(utilidades.porcentaje(10, 0))  # Error
except ValueError as e:
    print("Error:", e)