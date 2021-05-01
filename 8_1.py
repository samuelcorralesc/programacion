N=1

while N!=0:
    N=int(input())
    if N!=0:


        Cont=N
        for i in range (1, N+1): #para las filas
            for j in range (1, N+1): #para columnas
                if i==j or i==Cont:
                   print('#',end='')
                else:
                   print('0',end='') 
                Cont-=1
            print('\n',end='')
            Cont=N