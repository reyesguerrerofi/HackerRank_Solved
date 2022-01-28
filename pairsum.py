'''
5 5 ->
1 2 3 4 5

5 0
2 -3 3 3 -2
'''


s = [5,5]
arr = [1,2,3,4,5]


def pairSum(arr,s):
    res = []
    if s[0] == len(arr):
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                print(arr[i],arr[j])
                val = arr[i] +  arr[j] 
                if val == s[1] and arr[i]<=arr[j] and i!=j:
                    res.append([arr[i],arr[j]])
                
    else:
        print("El tamaño no corresponde debe ser: {0}".format(s[0]))
    
    return res

print(pairSum(arr,s))