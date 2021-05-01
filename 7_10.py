def fun(l,p):
    va=len(l)
    cont=0

    for v in range(0,va):
        r=l[v]
        cont+=r
        
    if cont==p:
        return True
    return False

l=[]
a=int(input())



for i in range(0,a):
    p=int(input())
    for j in range(1,p,1):
        if p%j==0:
    
            l.append(j)
    


    if fun(l,p):
         print(p,'es perfecto')

    else:
        print(p,'no es perfecto')
    l.clear()
