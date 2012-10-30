from swampy.TurtleWorld import *
import math

def spiral(t,n,length,angle):
    theta = 0.0
    a=2
    b=3
    for i in range(n):
        fd(t,length)
        dtheta = 1 / (a + b * theta)
        lt(t,angle)
        theta += dtheta
        

world = TurtleWorld()
bob = Turtle()

bob.delay = 0.001

spiral(bob, 1000, 3,5)

wait_for_user()