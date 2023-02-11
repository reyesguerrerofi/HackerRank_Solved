'''
Contador de vocales. Solo cuenta
las vocales minusculas
'''


def cuentaVocal(cadena):
	count = 0
	vocales = ["a","e","i","o","u","y"]
	for i in cadena:
		if i in vocales:
			count+=1
	return count


entradas = int(input())

for j in range(entradas):
	datos = input()
	resultado = cuentaVocal(datos)
	print(resultado,end=" ")




