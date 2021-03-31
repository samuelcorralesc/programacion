n=int(input())
n>1
if n%2==0:
    print(n,'es multiplo de 2')
elif n%3==0:
     print(n,'es multiplo de 3')

elif n%5==0:
    print(n,'es multiplo de 5')
elif n%7==0:
    print(n,'es multiplo de 7')
else:
    print(n,'no es multiplo de ninguno de los primeros cuatro primos')