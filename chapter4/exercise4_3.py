from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()

bob.delay = 0.001

def square(t,length):
    for i in range(4):
        fd(t,length)
        lt(t)

def polygonOrig(t,n,length):
    angle = 360.0/n
    for i in range(n):
        fd(t,length)
        lt(t,angle)
        
def circle(t,r):
    circumfrence = 2 *math.pi*r
    print circumfrence
    n = int(circumfrence/3)+1
    print n
    length = circumfrence/n
    print length
    polygon(t, n, length)

def arc(t,r,angle):
    arcLength = 2*math.pi*r*angle/360
    n = int(arcLength/3)+1
    step_angle =float(angle)/n
    arc_length =  arcLength/n
    polyline(t, n, arc_length, step_angle)

def CircleArc(t,r):
    arc(t, r, 360.0)
    
def polyline(t,n,length,angle):
    for i in range(n):
        fd(t,length)
        lt(t,angle)
def polygon(t,n,length):
    angle = 360.0/n
    polyline(t, n, length, angle)

    
    

#square(bob,50.543432)
#square(bob,55.564)

#polygon(bob, 25, 60)

#circle(bob, 100)

#arc(bob,55,180)

#CircleArc(bob,56)

#arc(bob, 100, 45)
#lt(bob,130)
#arc(bob,100,45)

wait_for_user()