from swampy.TurtleWorld import *
import math

def spiral(t,n,length,angle):
    for i in range(n):
        fd(t,length)
        lt(t,angle)
        angle = angle+(.5)
        

world = TurtleWorld()
bob = Turtle()

bob.delay = 0.01

spiral(bob, 70, 10,5)

wait_for_user()