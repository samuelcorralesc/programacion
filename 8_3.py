def fun (f,g):


    d=len(f)

    q=0


    for k in range (0,d):


        s=int(f[k])**d

        q +=s



    if q==g:


        return True


    return False
        



L=[]    


v=int(input())


for i in range (1,v+1):




    g=int(input())

    f=list(str(g))


    if fun(f,g):


        print(g,'es Armstrong')



    else:


        print(g, 'no es Armstrong')



        
    f.clear()