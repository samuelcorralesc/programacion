from datetime import datetime 

Ca=int(input())

for i in range (Ca):

    H=input()

    Hc=datetime.strptime(H, '%I:%M:%S %p')

    Con=Hc.strftime('%H:%M:%S')

    S=datetime.strptime(Con, '%H:%M:%S')

    G=((S.hour)*3600)+((S.minute)*60)+(S.second)
    
    P=G*100/86400
    print('Loading day ...',end=' ')
    print(round(P,3),end='%')
    print('\n',end='')