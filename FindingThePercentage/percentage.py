if __name__ == '__main__':
	n = int(input()) #Contador en n
    	student_marks = {} #Diccionario
    	calculo = []
    	for _ in range(n):
        	name, *line = input().split() #Name solo guarda una variable del split, *line o *args guarda una lista con cantidad indefinidas de variables
        	scores = list(map(float, line)) #Aplica a todo lo guardado en *line  float y list
        	student_marks[name] = scores
    	query_name = input() #Entrada de lo que se quiere regresar
    
   	for k,v in student_marks.items():
        	if k == query_name:
           		calculo = v
    	suma = sum(calculo)
    	promedio = suma / len(calculo)
    	formato = "{:.2f}".format(promedio) #Da un formato de 
    	print(formato)
