print("comparador de valores")
v1 =float(input("Escribe un valor "))
v2 =float(input ("Escribe el segundo valor "))
v3 =float(input("Escribe un tercer valor "))

if v1>v2 and v1>v3:
    print("el primer valor es el mayor")
else:
    if v2> v1 and v2>v3:
        print("el segundo valor es mayor")
    else:
        if v3> v2 and v3> v1:
            print("el tercer valor es el mayor")
            
c=input("quieres comparar mas valores?")