msj=open('mensaje.txt','r')


for val in msj:


    ent=len(val)


    print(val[-1:-ent-1:-1], end='')