from datetime import datetime

Da=int(input())

Conta=0

for i in range (Da):

    C=input()

    B=C.split()

    F=datetime.strptime(B[0], '%Y/%m/%d')
    M=F.month

    D=F.day
    T=int(B[1])

    y=F.year
    for i in range(1,T+1):

        A=y+i
        Ft=datetime(A,M,D)
        L=Ft.strftime('%A')
        #print(L)
        if L== 'Monday':
            Conta+=1

    print(Conta)

    Conta=0
    