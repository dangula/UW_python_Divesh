import math
from Foundation import ABS

def square_root(a):
    x = 1
    while True:
        print "x= ",float(x)
        y=float(x+(a/x))/2.0
        print "y = ",y
        if abs(y-x)<0.000001:
            break
        x = y


square_root(9)
