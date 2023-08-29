#Obtener un programa que permita liquidar los sueldos de los operarios de una fabrica.	

#Declaración de variables
nombre_operario= ""
sueldo_basico= 0.00
monto_premio=0.00
monto_adicional= 0.00
sueldo_total= 0.00

#Constantes
porcentaje_premio1=0.20
porcentaje_premio2=0.10
porcentaje_premio3=0.05
porcentaje_adicional=0.03

#Clave que me permite seguir o finalizar con el programa
clave="NO"
	    #Ciclo que me permite seguir o finalizar con el programa
while clave != "SI":
	#Ingreso y validaciones de datos del operario
	print ("Ingrese el nombre del operario: ")
	nombre_operario=input()

	print ("Ingrese el sueldo básico de cada operario: ")
	sueldo_basico=float(input())

	#Calcular por cada operario las horas que trabaja por dia y las unidades que produce en ese mismo dia
	#Defino las variables para mi nuevo ciclo
	contador=0
	sumatoria=0 
	unidades_producidas_xhora=0
	while contador < 5:
		#Se debe de ingresar las unidades que el operario produce en la 1ra hora y asi sucesivamente hasta la 5ta hora
		print ("Ingrese individualmente cuantas unidades produce el operario cada 1 hora:  ")
		unidades_producidas_xhora= int(input())

		contador=contador + 1
		sumatoria= sumatoria + unidades_producidas_xhora

	    #Monto premio que le pertenece a cada operario
	if sueldo_basico>=1 and sueldo_basico<=20000:
		monto_premio= porcentaje_premio1 * sueldo_basico
	else:
		if sueldo_basico>=20001 and sueldo_basico<=40000:
		    	monto_premio= porcentaje_premio2 * sueldo_basico
		else:
			if sueldo_basico>40000:
				 monto_premio= porcentaje_premio3 * sueldo_basico

		#Monto adicional que le pertenece a cada operario
	if sueldo_basico<40000:
		monto_adicional= porcentaje_adicional * sueldo_basico

		#Sueldo total que le pertenece a cada operario
		sueldo_total= sueldo_basico + monto_premio + monto_adicional

		#Salida por pantalla
		print ("1.Nombre del empleado: " ,nombre_operario)
		print ("2.Sueldo basico del operario: " ,sueldo_basico)
		print ("3.Las horas de trabajo son: " ,contador ,"horas")
		print ("4.Las unidades producidas por dias son: " ,sumatoria ,"unidades")
		print ("5.Monto del premio:$ " ,monto_premio)
		print ("6.Adicional por unidades producidas:$ " ,monto_adicional)
		print ("7.Sueldo total:$ " ,sueldo_total)

		#En caso de que el usario quiera finalizar el programa se ingresa "SI" por teclado, caso contrario el programa continua
		print ("Desea finalizar el programa? SI/NO")
		clave=input()

	