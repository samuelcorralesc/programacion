from datetime import datetime

Ca=int(input())

ContB=0

Acu=datetime.strptime('00:00:00', '%H:%M:%S')

Y=datetime.strptime('00:00:00', '%H:%M:%S')

for i in range (Ca):

    H=input()

    B=H.split(', ')


    if B[1]=='barberia':
        ContB+=1
        HF=datetime.strptime(B[3], '%H:%M:%S')
        HI=datetime.strptime(B[2], '%H:%M:%S')
        Ht=HF-HI
        Acu+=Ht
     
Tx=Acu-Y
Pro=Tx//ContB
Prom=Pro.seconds
Hour=Prom//3600
Min=(Prom%3600)//60
Seg=(Prom%3600)%60
print(ContB, 'veces')
print(Hour,'horas,',Min,'minutos,',Seg,'segundos')