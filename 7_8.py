from math import sqrt


def p(x):
    y=2*x+1

    return y


def a(b):
    c=3**b

    return c


def d(u):
    f=sqrt((5*u)+4)

    return f


l=int(input())
  

for x in range(0,l):
      g=float(input())

      print(p(a(d(g))))