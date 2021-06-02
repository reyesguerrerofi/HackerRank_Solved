if __name__ == '__main__':
	lista1 = []
    	lista3 = []
    	lista4 = []
    	respuesta = []
    	for _ in range(int(input())):
        	name = input()
        	score = float(input())
        	lista2 = [name,score]
        	lista1.append(lista2)
    	for i in range(0,len(lista1)):
        	lista3.append(lista1[i][1])
        	lista4.append(lista1[i][0])
    	records = dict(zip(lista4,lista3))
    	minimo = min(lista3)
    	for elemento in sorted(lista3):
        	if elemento == minimo:
            		lista3.remove(elemento)
    	minimo_guia = min(lista3)
    	for k,v in records.items():
        	if v == minimo_guia:
            		respuesta.append(k)
    	for j in sorted(respuesta):
        	print(j)

