from swampy.TurtleWorld import *
import math

def spiral(t,n,length,angle):
    for i in range(n):
        fd(t,length)
        lt(t,angle)
        angle = angle+(angle *.2)
        

world = TurtleWorld()
bob = Turtle()

bob.delay = 0.001

spiral(bob, 100, 10,5)

wait_for_user()