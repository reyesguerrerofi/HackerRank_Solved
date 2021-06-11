def inserta(argumento,lista):
    """Inserta un valor en una lista dado su posicion y el argumento
    Args:
        argumento ([list]): Lista con las operaciones a realizar
        contiene dos argumentos [0] y [1]. [0] es el index donde se inserta
        el argumento [1]
        lista ([list]): Lista a la que se le aplicaran las operaciones
    """
    lista.insert(argumento[0],argumento[1]) 
def imprime(argumento,lista):
    """Imprime la lista
    """
    print(lista)  
def remueve(argumento,lista):
    """Remueve elemento de la lista
    Args:
        argumento (list): Valor que se remueve
    """
    lista.remove(argumento[0])     
def append(argumento,lista):
    """Agrega elemento con operacion append a la lista
    Args:
        argumento (list): Argumento que se inserta
    """
    lista.append(argumento[0])  
def ordena(argumento,lista):
    lista.sort()  
def pop(argumento,lista):
    lista.pop()     
def reverse(argumento,lista):
    lista.reverse()    

if __name__ == '__main__':
    opciones = {  #Diccionario equivalente a switch
    'insert': inserta,
    'print' : imprime,
    'remove': remueve,
    'append': append,
    'sort'  : ordena,
    'pop'   : pop,
    'reverse': reverse
}
    N = int(input()) #Numero de instrucciones 
    lista_mov = [] #Lista de operaciones de lista
    lista_final = [] #Lista donde se opera
    lista_posi = [] #Lista de posiciones y argumentos
    j = 0 #Indice para ingresar argumentos
    for _ in range(N):
        instr,*line = input().split()
        movimientos = list(map(int,line))
        lista_mov.append(instr)
        lista_posi.append(movimientos)
    for i in lista_mov:
        opciones[i](lista_posi[j],lista_final)
        j+=1
