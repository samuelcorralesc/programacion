from datetime import datetime

V=0

B=0

Sw=0

Lw=0

Sl=0

Pt=0

Re=int(input())
for i in range(Re):
    Ne=input()
    G=Ne.split()
    S=G[1]
    H=datetime.strptime(S,'%H:%M:%S')
    #print (H)
    if H<= datetime.strptime('03:59:59','%H:%M:%S') and H>= datetime.strptime('00:00:00','%H:%M:%S'):
        V+=1
    elif H<= datetime.strptime('07:59:59','%H:%M:%S') and H>= datetime.strptime('04:00:00','%H:%M:%S'):
        B+=1
    elif H<= datetime.strptime('11:59:59','%H:%M:%S') and H>= datetime.strptime('08:00:00','%H:%M:%S'):
        Sw+=1
    elif H<= datetime.strptime('15:59:59','%H:%M:%S') and H>= datetime.strptime('12:00:00','%H:%M:%S'):
        Lw+=1
    elif H<= datetime.strptime('19:59:59','%H:%M:%S') and H>= datetime.strptime('16:00:00','%H:%M:%S'):
        Sl+=1
    elif H<= datetime.strptime('23:59:59','%H:%M:%S') and H>= datetime.strptime('20:00:00','%H:%M:%S'):
        Pt+=1
print('true vampires', V)
print('early birds', B)
print('sunny warmers', Sw)
print('lunch workers', Lw)
print('sunset lovers', Sl)
print('prime timers', Pt)