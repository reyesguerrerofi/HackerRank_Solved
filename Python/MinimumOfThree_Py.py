'''
Es similar al de Minimun of Two

se introduce el número de tripletes de datos que
se van a introducir.

El formato de entrada va a ser

3

12 14 2
234 -23 1
22 -23 -24

Salida: 2 -23 -24

'''

respuesta = []

rango = input()

for i in range(int(rango)):
	
	datos = input().split(' ')
	
	if (int(datos[0])<int(datos[1])) & (int(datos[0])<int(datos[2])):
		respuesta.append(datos[0])
	elif (int(datos[1])<int(datos[0])) & (int(datos[1])<int(datos[2])):
		respuesta.append(datos[1])
	else:
		respuesta.append(datos[2])

for j in respuesta:
	print(j)

'''
El autor del problema sugiere una respuesta más eficiente,
esta consiste en reducir la gran cantidad de comparaciones que hago.
Yo hago 4 en total.

Sin embargo se pueden usar dos usando una variable temporal que 
represente al valor minimo.
'''

#respuesta = []

#rango = input()

#for i in range(int(rango)):
#	
#	datos = input().split(' ')
#	
#	minimo = int(datos[0]) #Este arbitrariamente lo ponemos como el minimo aunque no sea verdad
#	
#	if(minimo>int(datos[1])):
#		minimo = int(datos[1])
#	if(minimo>int(datos[2])):
#		minimo = int(datos[2])
#	
#	respuesta.append(minimo)
#	
#for j in respuesta:
#	print(j)

