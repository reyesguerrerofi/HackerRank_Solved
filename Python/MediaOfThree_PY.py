'''
El medio de 3 números

7 3 5 --> el medio es 5
'''

casos = int(input())

for i in range(casos):

	datos = input().split(" ")
	datos = list(map(int,datos))

	maximo = datos[0]
	minimo = datos[0]

	for j in range(0,len(datos)-1):
		if maximo<datos[j+1]:
			maximo = datos[j+1]
		if minimo>datos[j+1]:
			minimo = datos[j+1]


	for k in datos:
		if (k!=maximo) & (k!=minimo):
			print(k, end=" ")
