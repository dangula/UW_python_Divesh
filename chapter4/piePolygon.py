from swampy.TurtleWorld import *
import math

    
def piePolygon(t, n, r):
    """Draws a pie divided into radial segments.

    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isoscelesTriangle(t, r, angle/2)
        lt(t, angle)


def isoscelesTriangle(t, r, angle):
    """Draws an icosceles triangle.

    The turtle starts and ends at the peak, facing the middle of the base.

    t: Turtle
    r: length of the equal legs
    angle: peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    rt(t, angle)
    fd(t, r)
    lt(t, 90+angle)
    fd(t, 2*y)
    lt(t, 90+angle)
    fd(t, r)
    lt(t, 180-angle)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001

#Figure 4.2.1
#piePolygon(bob, 5, 40)

#Figure 4.2.2
#piePolygon(bob, 6, 40)

#Figure 4.2.3
piePolygon(bob, 7, 40)
die(bob)

wait_for_user()