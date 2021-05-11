ent=int(input())
m1={}
for i in range(0,ent):
    q1=input()
    q1=q1.split()
    q2=q1[0]
    q3=q1[1]
    m1[q2]=q3
e2=int(input())
for e in range (0,e2):
    m3=input()
    if m3 in m1:
        print(m1[m3])
    else:
        print('palabra no encontrada')