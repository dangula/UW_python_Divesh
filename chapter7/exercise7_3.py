import math

def square_root(a):
    x = 1
    while True:
        y=float(x+(a/x))/2.0
        if abs(y-x)<0.000000001:
            break
        x=y
    return y



square_root(16)

def test_square_root():
    n=1.0
    while n<10:
        a = square_root(n)
        b = math.sqrt(n)
        print n,"  ",repr(a)," "*(30-len(repr(a))),repr(b)," "*(30-len(repr(b))),abs(a-b)
        n=n+1

test_square_root()
