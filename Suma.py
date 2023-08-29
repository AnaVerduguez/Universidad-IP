#Declaracion de variables. Inicializo mis variables.
#Variables -> tipo de datos-> entero/real/caracteres(string)

num1= 0 #Le asigna un tipo de dato entero 
num2= 0
nombre= ""
suma=0.00

#Ingreso de datos
print("Ingrese un numero:")
num1= int(input)

print("Ingrese otro numero:")
num2= int(input)

#Proceso
suma=(num1+num2/2)

#Salida de datos por pantalla 
print("El promedio es",suma)

#Validacion
while num1< 0:
    print("Ingrese un num")
    num= int(input())

    #mostrar error
    if num <0:
        print("Error ingrese un numero mayor a 0")
