def fun(x):

    ent=len(x)

    num=0

    for e in range(0,ent-1):


    
        var1=x[e]


        var2=x[e+1]



        if (var1[-2]+var1[-1])==(var2[0]+var2[1]) or (var1[-3]+var1[-2]+var1[-1])==(var2[0]+var2[1]+var2[2]):
           
           
            num+=1
    if num==(ent-1):



        
        
        
        return 1


    else:


        return 0





A=open('cadena.txt','r')



for ren in A:



    er=ren.split()


    Rif=fun(er)


    if Rif==1:


        print('cadena completa')


    else:


        print('cadena rota')



    er.clear()
    

A.close()