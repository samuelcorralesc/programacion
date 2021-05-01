def sc(y):


    Li=[2,1]


    while Li[-1]<=y:

        Ne=Li[-1]+Li[-2]

        Li.append(Ne)



    return Li


An=int(input())


Br=int(input())


Jt=sc(Br+1)

numm=0

for o in range (An,Br+1):


    if o in Jt:


        numm+=1



print(numm)