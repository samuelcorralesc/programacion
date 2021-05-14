ent=int(input())


for i in range(0,ent):


    q1=int(input())


    en= str()


    A=str()


    for j in range (1,q1+1):


        L=input()


        A+= L + '\n'



    ar=''


    T=(q1//2)


    for h in list(range(q1)):


        for k in list(range(q1)):


            if h==k:

                ar+='#'


            elif k==q1-h-1:


                ar+='#'
                
            elif h==T or k==T:


                ar+='+'


            else:


                ar+='0'


        ar+= '\n'



    C=ar

    if C==A:


        print('Bandera britanica')
    else:

        print('Ni idea')