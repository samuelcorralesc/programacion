cant=int(input())

do=cant-1
re=do+1



lista=[]




for i in range(0,re):




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