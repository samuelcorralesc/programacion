H = int(input())
M = int(input())
N = str(input())
if N == 'am':
    if H == 12:
        X = 1440-M
        print('Faltan', X, 'para las 12')
    elif H != 12:
        X = ((24-H)*60)-M
        print('Faltan', X, 'para las 12')
else:
    if H == 12:
        X = 720-M
        print('Faltan', X, 'para las 12')
    elif H != 12:
        X = ((24-H-12)*60)-M
        print('Faltan', X, 'para las 12')