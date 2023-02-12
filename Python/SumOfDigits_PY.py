'''
Suma de digitos

1767 -> 1 + 7 + 6 + 7 = 21

no debe ser usado ninguna funcion para
convertir el int en str (asi seria mas facil)

Problema -> se reciben 3 números 

11 23 456 -> A B C

A y B se multiplican A*B

C se suma al final A*B+C

11*23+456 = 709

el valor obtenido se debe sumar cada uno de sus digitos

7 + 0 + 9 = 16
'''
cantidad = int(input())
for i in range(cantidad):
	datos = input().split(" ")
	datos = list(map(int,datos))
	numero = (datos[0]*datos[1]) + datos[2]
	division = numero
	respuesta = 0
	while division != 0:
		residuo = division%10
		division = division//10
		respuesta = respuesta + residuo
	print("\n")
	print(respuesta, end= " ")

