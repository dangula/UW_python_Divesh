from swampy.TurtleWorld import  *
import math

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)
    
def petal(t,r,angle):
    """
    Draws a single petal for a flower, which is basically 2 identical arcs facing each other
    
    t: Trutle
    r: radius of arc
    angle: angle of arc
    """
    arc(t, r, angle)
    lt(t,180-angle)
    arc(t, r, angle)

def flower(t,n,r,angle):
    """
    Draw a flower of n petals, each petal is of lenght 'r'
    and Angle 'angle'
    
    t: Trutle
    n: number of petals
    r: radius of arc
    angle: angle of arc
    """
    turnangle = 360.0/n
    for i in range(n):
        petal(t, r, angle)
        lt(t,180-angle)
        rt(t,turnangle)
        


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

#Figure 4.1.1
#flower(bob,7, 70, 60)


#Figure 4.1.2
#flower(bob,10, 70, 80)

#Figure 4.1.3
flower(bob, 20, 150, 25)

wait_for_user()
    