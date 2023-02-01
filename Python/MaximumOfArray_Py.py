'''
Problema de busqueda lineal para saber cual es el mayor y el menor
valor en un array.

Se introduce el número de datos en el array
y se devolveran el valor mas alto y el minimo

300 2 1 3 4 5 7 34 567

567 1 -> mayor y menor

'''


def maximo(array):
	
	maximo = int(array[0])
	for i in range(len(array)-1):
		if maximo<int(array[i+1]):
			maximo = int(array[i+1])
	return maximo
	
	
def minimo(array):
	
	minimo = int(array[0])
	for i in range(len(array)-1):
		if minimo > int(array[i+1]):
			minimo = int(array[i+1])
	return minimo

datos = input().split(' ')

respuesta1 = maximo(datos)
respuesta2 = minimo(datos)

print(respuesta1, respuesta2)

'''
Arriba esta una solución en dos partes, si funciona pero 
es se puede trabajar con un solo loop ahorrando recursos.
'''

valor_maximo = int(datos[0])
valor_minimo = int(datos[0])

for j in range(len(datos)-1):
	if valor_maximo<int(datos[j+1]):
		valor_maximo = int(datos[j+1])
	elif valor_minimo>int(datos[j+1]):
		valor_minimo = int(datos[j+1])

print(valor_maximo, valor_minimo)


