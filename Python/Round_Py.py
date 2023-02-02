'''
Se introducen un par de valores,
estos se dividen entre si (el primero
sobre el segundo), el valor resultante debe
ser redondeado al entero mas cercano.

Si el valor exactamente contiene 0.5 
debe ser sumado por 0.5
en el negativo debe ser al entero mas cercano

	-23.5 -> -23
'''


pares_i = int(input())
respuesta = []


for i in range(pares_i):

	datos = input().split(" ")
	datos = list(map(int,datos))
	
	div = datos[0]/datos[1]
	#Numero negativo
	
	if ((datos[0]<0)&(datos[0]>0)) | ((datos[1] < 0)&(datos[0]>0)):
		if div<0:
			division = datos[0]/datos[1]
			frac = (division*-1)%1
			if frac<0.5:
				resultado = division + frac
				respuesta.append(int(resultado))
			else:
				resultado = datos[0]//datos[1]
				respuesta.append(int(resultado))
	#Numero positivo
	elif div>0:
		division = datos[0]/datos[1]
		entero = datos[0]//datos[1]
		frac = division%1
		
		if frac>=0.5:
			complemento = 1 - frac
			resultado =  division + complemento
			respuesta.append(int(resultado))
		else:
			resultado = division - frac
			respuesta.append(int(resultado))
			
for j in respuesta:
	print(j)
	
'''
En este lenguaje y en otros ya existe una 
funcion llamada round asi que no es necesario 
agregar tanto rollo
aun asi lo hice asi para entender como funciona el 
redondeo

'''
