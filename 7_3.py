 

def rec(X):

    if X < 1:

        return 0

    return 6*X + rec(X-1)

 

print(rec(6)-15)

 