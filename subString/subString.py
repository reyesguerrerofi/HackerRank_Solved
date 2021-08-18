"""
#Toma el indice de todas las ocurrencias del primer caracter del substring
#Con esos indices se ejecuta el ciclo for para introducir a la funcion el valor del indice y las cadenas
#Recorta la cadena original a partir del valor del indice, si el tamaño de la cadena es mayor o igual al del
substring se realiza la busqueda
#Se realiza un ciclo while para seguir realizando la operacion hasta que se recorra todo el indice de substring
#
"""
def count_substring(string, sub_string):
    indexes = []
    aux = []
    final = []
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            indexes.append(i)
    for j in indexes:
        a = busqueda(j,string,sub_string)
        aux.append(a)
    final = [i for i in aux if i != 0]    
    return len(final)
def busqueda(n,string,sub_string):
    i = 0
    new_string = string[n:]
    size_string = len(sub_string)
    size_string1 = len(new_string)
    if size_string <= size_string1:
        while i < size_string:
            if new_string[i] == sub_string[i]:
                i += 1
                continue
            else:
                return 0
    else:
        return 0
        

string = ""
sub_string = ""

respuesta = count_substring(string,sub_string)