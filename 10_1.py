cant=int(input())





lista=[]




for i in range(0,cant):




    otra=input()



    otra=otra.split()



    lista.append(otra)





list2=[]




for re in lista:



    if re[2]=='positiva':




        Edad=int(re[1])



        Pizza=int(re[3])



        res=[Pizza,Edad]


        list2.append(res)


list2.sort(reverse=True)


for uu in list2:

    
    print(uu[1],'POSITIVA', uu[0])