listaa = []



while True:


    entraa= int(input())

    listaa+=[entraa]



    if entraa==-1:
        break


listaa.remove(-1)

def par(x):

    if x%2==0:

        return True
    return False



for i in range(len(listaa)):

    if par(listaa[i])== True:

        entraa2=listaa[i]

        entraa1=entraa2

        contad=1

        cuenta=0

        
        hiper=0


        while entraa1>10:
            entraa1=entraa1//10


            if entraa1==10:
                contad+=1
            contad+=1


        rango=range(contad)

        lista= list(rango)


        for j in range(contad):


            digito=10**contad/10**cuenta
            opee= int((entraa2/digito)*10)
            cuenta+=1


            if opee>=10:
                opee1= int(round(((opee/10)-opee//10)*10,0))
                lista[j]= opee1


            else:
                lista[j]=opee


        for k in range(len(lista)):


            if par(lista[k])== True:
                hiper+=1

            else:
                hiper+=0

                
        if hiper==contad:
            print('Hyperpar')


        else:
            print('No es hyperpar')


    else:
        print('No es hyperpar')