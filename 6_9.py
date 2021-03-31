F=[]
Cont=0
k=0
i=0
while True:
    N=int(input())
    if N!=0:
        F.append(N)
    else:
        break
J=len(F)
for i in range(0,J):
    while k<J:
        if(F[i]+F[k]==1995):
            Cont+=1
            break
        k+=1
    k=0
print(int(Cont/2))