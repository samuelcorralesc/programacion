L = int(input())
H = int(input())

for i in range(H):

    for j in range(L):

        if i == (H-1)/(2)  or j == (L-1)/(2):
            print("+", end = "")
        else:
            print("0", end = "")

    print("")