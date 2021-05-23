from datetime import datetime
num=int(input())
for i in range(num):
    ru=input()
    G=ru.split()
    FecI=datetime.strptime(G[1],'%Y-%m-%d')
    FecF=datetime.strptime(G[2],'%Y-%m-%d')
    dife=FecF-FecI
    print(dife.days, 'dias',end=' = ')
    print(dife.days*24, 'horas',end=' = ')
    print(dife.days*24*60, 'minutos', end=' = ')
    print(dife.days*24*60*60, 'segundos')