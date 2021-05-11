val=int(input())
lis=[]

for i in range(0,val):

    ent=input()
    ent=ent.split(', ')
    lis.append(ent)



l2=[]
for q in lis:

        N0=int(q[0])

        N1=round((int(q[1])/9)*5,1)

        N2=round((int(q[2])/11)*5,1)

        N3=round((int(q[3])/12)*5,1)

        N4=round((int(q[4])/8)*5,1)

        N5=round((int(q[5])/12)*5,1)

        N6=round((int(q[6])/9)*5,1)

        N7=round((int(q[7])/11)*5,1)

        N8=round((int(q[8])/8)*5,1)

        N9=round((int(q[9])/11)*5,1)

        N10=round((int(q[10])/10)*5,1)

        N11=round((int(q[11])/9)*5,1)

        N12=round((int(q[12])/10)*5,1)

        resuu=[N0,N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11,N12]

        l2.append(resuu)


fin=[]
var=0

for t in l2:
    for i in range(1,13):
        var+=t[i]
    var=round(var/12,1)
    re=(t[0],var)
    fin.append(re)
    var=0

fin.sort()
for po in fin:
    print(po[0],po[1]) 
