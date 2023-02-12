'''
El medio de 3 números

7 3 5 --> el medio es 5
'''

casos = int(input())

for i in range(casos):
	
	datos = input().split(" ")
	datos = list(map(int,datos))
	
	maximo = 0
	minimo = 0
	medio_1 = 0
	medio_2 = 0
	for j in range(0,len(datos)-1):
		if datos[j]>datos[j+1]:
			maximo = datos[j]
			medio_1 = datos[j+1]
		if datos[j]<datos[j+1]:
			minimo = datos[j]
			medio_2 = datos[j+1]
	
		print("\n")
		print(medio_1,medio_2)
