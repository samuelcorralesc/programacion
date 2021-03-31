p=int(input())

if p>=50000:
    queda=p//50000
    print(str(queda),'de $50000')
    p=p%50000

if p>=20000:
    queda=p//20000
    print(str(queda),'de $20000')
    p=p%20000

if p>=10000:
    queda=p//10000
    print(str(queda),'de $10000')
    p=p%10000

if p>=5000:
    queda=p//5000
    print(str(queda),'de $5000')
    p=p%5000

if p>=2000:
    queda=p//2000
    print(str(queda),'de $2000')
    p=p%2000

if p>=1000:
    queda=p//1000
    print(str(queda),'de $1000')
    p=p%1000






