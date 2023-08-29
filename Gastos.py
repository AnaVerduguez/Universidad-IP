categoria=-1
monto=-1.00
cant_gastos=0
cant_ingresos=0
total_gastos=0.00
total_ingresos=0.00
saldo=0.00
	
while categoria != 3:

    #Inicialización de variables
    categoria=-1
    monto=-1.00

    #ngreso y validación de categoria
    while categoria <1 or categoria >3:
        #Dibujo un Menu de opciones
        print(" M E N U ")
        print("1. Cargar gasto")
        print("2. Cargar ingreso")
        print("3. Salir")
        categoria=int(input())

	#Mensaje de error
        if categoria <1 or categoria >3:
            print("Error - ingrese una categoria valida entre 1 y 3")
		
    #Verificar que el usuario no eligio salir
    if categoria != 3:

        #Ingreso y validación del monto
        while monto <0.00:
            print("ingrese monto")
            monto=float(input())
				
	    #Mensaje de error
            if monto < 0.00:
                print("Error - ingrese un monto válido")

	#Determinar la opcion elegida (Ingreso o Gasto)
        #Caso de que sea gastos
        if categoria==1:
            cant_gastos=cant_gastos +1 #Incrementar la cantidad de gastos
            total_gastos=total_gastos + monto #Acumular los gastos

        #Caso de que sea ingresos
        if categoria==2:
            cant_ingresos=cant_ingresos +1 #Incrementar la cantidad de ingresos
            total_ingresos=total_ingresos + monto #Acumular los ingresos
	
#Salida y cálculo del saldo
print("El saldo es :",total_ingresos-total_gastos)
