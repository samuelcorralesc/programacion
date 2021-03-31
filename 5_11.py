C = int(input())  
                 
for i in range(C):
    A = int(input())
    P = int(input())
    Q = int(input())

    a = A 
    p = P  

    for i in range(p, Q+1): 
        if a % i == 0: 
            a = a//i
            p += 1
        else:
            break


    if p == (Q + 1):
        print(A, "es polifactor entre", P, "y", Q)
    else:
        print(A, "no es polifactor entre", P, "y", Q)