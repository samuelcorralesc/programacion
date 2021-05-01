def f(xi):
    J=[1]
    cont=0
    while J[-1]<= xi:
        for i in range (1,J[-1]+1):
            if J[-1]%i==0:
                cont+=1
        J.append(J[-1]+cont)
        cont=0
    return J

W=f(1E4)
xi=1
while xi!=0:
    xi=int(input())
    if xi!=0:
        if xi in W:
            print('Pertenece a la serie de Julianachi')
        else:
            print('No pertenece a la serie de Julianachi')