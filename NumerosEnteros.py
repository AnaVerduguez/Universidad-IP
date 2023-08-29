#Declaración de variables
nro=-1
contador=1
sumatoria=0
	
#Ingresar tres numeros reales positivo
while contador<=3:

    #Ingreso y validación de datos
    while nro <0:
        print("Ingrese un numero positivo")
        nro=int(input())

        #Mensaje de error
        if nro <0:
            print("Error ingrese un numero positivo")

    #incrementar la variable contador en una unidad
    contador=contador +1

    #Acumulo la sumatoria de los números
    sumatoria=sumatoria + nro

    #Inicialización de número
    nro=-1

#Salida por pantalla
print("La sumatoria es: ",sumatoria)
