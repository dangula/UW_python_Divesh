import math

class point(object):
    def __init__(self,x=0,y=0):
        """Exercise 17_2"""
        self.x = x
        self.y = y
    def __str__(self):
        """Exercise 17_3"""
        return "cordinates of point are x=%g and y=%g" %(self.x,self.y)
    
    def __add__(self,other):
        """Exercise 17_4 """
        newPoint = point()
        newPoint.x = self.x+other.x
        newPoint.y = self.y+other.y
        return newPoint
        

def pointDifference(p1,p2):
    return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)


if __name__ == "__main__" :
    p1 = point()
    p2 = point(3,4)
    print str(p2)
    print "Difference between p1 and p2 is : "+ repr(pointDifference(p1, p2))
    
    p3 = point(1,2)
    p4 = point(3,4)
    
    p5 = p3+p4
    print str(p5)
