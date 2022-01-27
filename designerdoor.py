
'''Mat size must be N X M (N is an odd natural number, and M is 3 times N
.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

'''
N = 7
M = (N*3)
T = "WELCOME"
print(N,M)#N alto, M ancho

def door(N,M,T):
    #Uso de rjust,ljust,center etc
    tramo = (M-3)/2
    for i in range(0,N):
        
            print(M*"-")
            print(i*3*".|.")
            M = M - 6




door(N,M,T)