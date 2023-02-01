'''
Dos listas del mismo tamaño

A = [10,2,13,4]

B = [9,3,11,5]

Comparar los valores de cada indice entre si y el menor de los 
dos agregarlo en una nueva lista.

C = [9,2,11,4]

CodeAbbey lo solicita con la introducción del numero de elementos a introducir y el par que se comparara

3
5 3
2 8
100 15

Salida 3,2,15
'''

#A = [10,2,13,4]
#B = [9,3,11,5]
#C = []

#for i in range(len(A)):
#	if A[i] > B[i]:
#		C.append(B[i])
#	else:
#		C.append(A[i])
#		
#print(C)

#Modo de CodeAbbey
rango = input()

for i in range(int(rango)):
	valores = input().split(' ')
	
	if int(valores[0])>int(valores[1]):
		C.append(valores[1])
	else:
		C.append(valores[0])

for j in C:
	print(j)
