def funcionA(N):

    return N*2

 

def funcionB(N):

    return N**2

 

def funcionC(N):

    N -= 12

 

N = 4

X = funcionA(N)

N += funcionB(N)

funcionC(N)

print(N)