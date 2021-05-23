en=int(input())
v={}
for i in range(en):
 ventas=input().split(":")
 alias=ventas[0]
 cantidad=int(ventas[1])
 if alias not in v:
  v[alias]=cantidad
 else:
  v[alias]+=cantidad
  primero=max(v,key=lambda en:v[en])
print("El vendedor del mes es" , primero)