nombre=""
edad=0
promedio=0.00
continuar="S"

while continuar=="S":
    print("Ingrese su nombre")
    nombre=input()

    print("Ingrese su edad")
    edad=int(input())
    
    print("Ingrese su promedio de notas")
    promedio=float(input())

    print("Nombre: ",nombre)
    print("Edad: ",edad)
    print("Promedio: ",promedio)

    if edad >=21:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

    print("Desea continuar S/N")
    continuar=input()

    


