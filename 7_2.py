def alfa(X):
    m = X - 3
    return 3*[m]

def beta(Y):
    n = len(Y)
    s = 0
    for e in Y:
        s += e*n
        n -= 1
    return s    

L = [6, 3, 8, 4, 9]
print(alfa(beta(L)))

