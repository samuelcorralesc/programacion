def f(x):



    var=len(x)



    conta=0


    wi=[int(x) for x in x]


    for i in range (1,6):



        if i in wi:

            conta+=1
    if conta==5:


        return True


    return False

Nu=1

while Nu!=0:

    Nu=int(input())

    if Nu!=0:


        x=list(str(Nu))


        if f(x):


            print('Multidigito')


        else:

            print('No es multidigito')


    x.clear()