from swampy.TurtleWorld import *

def drawKochCurve(t,x):
    if x<3:
        fd(t,x)
        return
    drawlen=x/3.0
    drawKochCurve(t, drawlen)
    lt(t,60)
    drawKochCurve(t, drawlen)
    rt(t,120)
    drawKochCurve(t, drawlen)
    lt(t,60)
    drawKochCurve(t, drawlen)

def drawSnowFlake(t,size,sides):
    angle = 360.0/sides
    for i in range(sides):
        drawKochCurve(t, size)
        lt(t,angle)
    
world =TurtleWorld()
bob = Turtle()
bob.delay=0.001

#drawKochCurve(bob, 100)

drawSnowFlake(bob, 50, 3)
die(bob)

wait_for_user()
    