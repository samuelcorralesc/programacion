Lis=[]    


Num=int(input())



cont=0


d,e=0,0


for i in range (1,Num+1):




    Xi=float(input())
    Lis.append(Xi)
    Hi=len(Lis)


for i in range (0,Hi-1):


    for k in range(0,i+1):


        s=Lis[k]

        d +=s
        #print(k,s,d)
    for j in range (i+1,Hi,1):

        w=Lis[j]


        e +=w


    if d==e:
        cont+=1
    d,e=0,0
print(cont)