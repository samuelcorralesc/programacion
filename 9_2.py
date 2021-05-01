texto = 'fundamentos de programacion'

sep = '_'

end = ' !'

fib = [0,  1,  1,  2,  3,  5,  8, 13, 21]

num = 76731

lista = []

for i in fib:

    lista.append(texto[i])

msg = ''

while num > 1:

    if num > 10:

        msg += (lista[num%10] + sep)

    else:

        msg += lista[num%10]

    num //= 10

msg += end

print(msg)