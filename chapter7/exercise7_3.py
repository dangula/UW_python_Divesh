import math

def square_root(a):
    x = (a+1)/3+1
    while True:
        y=float(x+(a/2.0))/2.0
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
        print n," ",a,"    ",b,"    ",abs(a-b)
        n=n+1

test_square_root()
