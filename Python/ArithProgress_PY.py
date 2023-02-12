'''
Progresión aritmetica

Basicamente son las series númericas.

En este caso se trata cuando los numeros 
se incrementan de la siguiente manera

A + (A + B) + (A + 2B) + (A + 3B) +...

EJEMPLO: A = 5, B = 2, N = 3

(5+0(B)) + (5+1(B))+(5+2(B))
5+(5+2)+(5+2(2))--> se aplica solo 3 veces la operacion
'''



casos  = int(input())

for i in range(casos):
	
	datos = input().split(" ")
	datos = list(map(int,datos))
	
	prog = 0
	A = datos[0]
	B = datos[1]
	N = datos[2]
	
	for j in range(N):
		prog = prog + (A + (B)*j)
	
	print(prog,end=" ")
