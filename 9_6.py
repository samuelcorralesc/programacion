ent=int(input())
for i in range(1, ent+1):
    M=input()
    CF=(M.count('F'))
    CM=(M.count('M'))
    if CF==CM:
        print('Es posible hacer un unico circulo')
    else:
        print('No es posible')