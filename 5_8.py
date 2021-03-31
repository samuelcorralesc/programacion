numero=int(input())
digitos=1
while numero>10:
    numero//=10
    digitos+=1

print(digitos)
