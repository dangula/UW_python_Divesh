import math

def square_root(a):
    x = (a+1)/3+1
    while True:
        print "x= ",float(x)
        y=float(x+(a/2.0))/2.0
        print "y = ",y
        if abs(y-x)<0.0000001:
            break
        x = y


square_root(4)
