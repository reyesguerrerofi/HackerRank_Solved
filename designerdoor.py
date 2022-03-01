
'''Mat size must be N X M (N is an odd natural number, and M is 3 times N
.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

'''
N = 11
M = (N*3)
T = "WELCOME"
#print(N,M)#N alto, M ancho

def door(N,M,T):
    A = 1
    for i in range(0,N):
        
        #L = 3 * A
        #tramo = (M-L)/2
        #tramo1 = (M-len(T))/2
        if i < (N-1)/2 :
            L = 3 * A
            tramo = (M-L)/2
            tramo1 = (M-len(T))/2
            print("-"* int(tramo) + ".|."* int(A) + "-"* int(tramo) )
            #print(L,tramo,A)
            A += 2 
        elif i == (N-1)/2:
            print("-"*int(tramo1) + T + "-"*int(tramo1))     
        elif i > (N-1)/2:
            print("-"* int(tramo) + ".|."* int(A-2) + "-"* int(tramo))
            tramo = tramo + 3
            A = A - 2





door(N,M,T)