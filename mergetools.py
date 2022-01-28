'''
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

len(s)/3 = 3
No se pueden repetir los valores, solo con la primera ocurrencia
AAB ->AB
CAA -> CA
ADA -> AD

'''
import numpy as np
s = "AABCAAADA"
k = 3
u = []

div = int(len(s)/k)

u = [s[i:i+div] for i in range(0,len(s),div)]
print(u)

u_n =[None]*div

for l in u:
    for i in range(len(l)):
        if l[i] not in l:
            u_i = l[i]
print(u_n)