v=(int(input()))
x=v+1
y=v-1
if v==3:
   print('El numero 3 es el mejor')

elif v%3==0:
   print('El numero',v,'es multiplo de 3. Y el numero 3 es el mejor')

else:
    if x%3==0:
         print('El numero',v,'no es multiplo de 3, pero si le sumas 1 el resultado si lo es. Y el numero 3 es el mejor')
    elif y%3==0:
          print('El numero',v,'no es multiplo de 3, pero si le restas 1 el resultado si lo es. Y el numero 3 es el mejor')  




