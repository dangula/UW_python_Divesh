from swampy.World import World
import math  
#===============================================================================
# world = World()
# canvas = world.ca(width=500, height=500, background='white')
# canvas.rectangle(bbox, outline='black', width=6, fill='green4')
# canvas.circle([-25,0], 70, outline=None, fill='red')
# world.mainloop()
#===============================================================================

class point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
class rectangle(point):
    def __init__(self,height=0,width=0,x=0,y=0):
        self.height = height
        self.width = width
        self.corner = point(x,y)
        
class circle(point):
    def __init__(self,radius=1,x=0,y=0):
        self.radius = radius
        self.center = point(x,y)
        
def draw_rectangle(rect,canvas,color):   
    RCorner = point(rect.corner.x+rect.width,rect.corner.y+rect.height)
    bbox = [[rect.corner.x,rect.corner.y],[RCorner.x,RCorner.y]]
    
    canvas.rectangle(bbox,color)

def draw_circle(circ,canvas,color):
    canvas.circle([circ.center.x,circ.center.y],circ.radius,color)

def draw_equilatralTriangle(point1,length,canvas,color):
    point2 = point(point1.x,point1.y+length)
    dX = point1.x - point2.x;
    dY = point1.y - point2.y;
    x3 = (math.cos(60*math.pi/180.0) * dX - math.sin(60*math.pi/180.0) * dY) + point2.y;
    y3 = (math.sin(60*math.pi/180.0) * dX + math.cos(60*math.pi/180.0) * dY) + point2.x;
    
    point3 = point(x3,y3)
    
    points = [[point1.x,point1.y],[point2.x,point2.y],[point3.x,point3.y]]
    canvas.polygon(points, color)
    

def draw_czechFlag(basePoint,canvas):
    redRect = rectangle(50,200,basePoint.x,basePoint.y)
    whiteRect = rectangle(50,200,basePoint.x,basePoint.y+50)
    
    draw_rectangle(redRect, canvas, "red")
    draw_rectangle(whiteRect, canvas,"white")
    draw_equilatralTriangle(basePoint, 100, canvas, "blue");
    
if __name__ == "__main__" :
    world = World()
    canvas = world.ca(width=500, height=500, background='white')
    rect = rectangle(50,100,-100,50)
    circ =circle(50,60,90)
    draw_rectangle(rect, canvas,"blue")
    draw_circle(circ, canvas, "#ffff00")
    basePoint  = point(0,-100)
    draw_czechFlag(basePoint,canvas)

    world.mainloop()
    
    