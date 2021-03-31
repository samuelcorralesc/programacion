a=input()
b=input()

if a=='piedra' and b=='piedra':
    print('empate')
if a=='papel' and b=='papel':
    print('empate')
if a=='tijera' and b=='tijera':
    print('empate')
if a=='piedra' and b=='papel':
    print('papel vence piedra')
if a=='papel' and b=='piedra':
    print('papel vence piedra')
if a=='tijera' and b=='papel':
    print('tijera vence papel')
if a=='papel' and b=='tijera':
    print('tijera vence papel')
if a=='tijera' and b=='piedra':
    print('piedra vence tijera')
if a=='piedra' and b=='tijera':
    print('piedra vence tijera')