H = int(input())
M = int(input())
if H == 12:
    if M == 0:
        print(H, ':', M, sep = '')
    elif M != 0:
        MR = 60-M
        print(H, ':', MR, sep = '')
elif 0<H<=6:
    HR = 12-H
    if M == 0:
        print(HR, ':', M, sep = '')
    elif M != 0:
        MR = 60-M
        print(HR, ':', MR, sep = '')

if 6<H<=10:
    HR = 11-H
    if M == 0:
        print(HR, ':', M, sep = '')
    elif M != 0:
        MR = 60-M
        print(HR, ':', MR, sep = '')

if 10<H<=12:
    HR = H+1
    if M == 0:
        print(HR, ':', M, sep = '')
    elif M != 0:
        MR = 60-M
        print(HR, ':', MR, sep = '')