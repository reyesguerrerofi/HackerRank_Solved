data = input().split(" ")
data_conv = list(map(int,data))
size = data_conv[0]
resultado = []

for i in range(1,size+1):

	tempCelcius = round((data_conv[i]-32)*(5/9))
	resultado.append(tempCelcius)


for j in resultado:
	print(j)



#print(round(tempCel),end=' ')

#Esta es una mejor forma de imprimir sin guardar algo en una lista.
