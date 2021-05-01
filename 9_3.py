def fun(ar):
    if ar[-2]=='i' and ar[-1]=='x':
        return 'Galo'
    if ar[-2]=='u' and ar[-1]=='s':
        return 'Romano'

    if ar[-2]=='a' and ar[-1]=='s':
        return 'Griego'
    if ar[-2]=='i' and ar[-1]=='c':
        return 'Godo'
    if ar[-2]=='a' and ar[-1]=='f':
        return 'Normando'
    if (ar[-1]=='s' and ar[-2]=='i') or (ar[-1]=='x' and ar[-2]=='a'):
        return 'Breton'
    if ar[-1]=='z' and ar[-2]=='e':
        return 'Hispano'
    if ar[-1]=='a':
        return 'Indio'
    return 'Desconocido'
            

p=int(input())
for i in range(1, p+1):
    ar=input()
    print(fun(ar))
