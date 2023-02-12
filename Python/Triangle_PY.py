'''
Triangulos

Decir si dados tres segmentos
con sus respectivas medidas
el armado de un triangulo es posible

Propuesta:

-Existe una propiedad que dice que la suma de dos lados
siempre es mayor al tercer lado. Por lo que si
en algun momento no se cumple la condicion el triangulo
no es posible.


'''
casos = int(input())


for i in range(casos):
	datos = input().split(" ")
	datos = list(map(int,datos))
	
	A = datos[0]
	B = datos[1]
	C = datos[2]
	
	test_1 = A + B 
	test_2 = A + C
	test_3 = C + B
	
	if (test_1 > C) & (test_2 > B) & (test_3 > A):
		print("1", end=" ")
	else:
		print("0", end=" ")
		
