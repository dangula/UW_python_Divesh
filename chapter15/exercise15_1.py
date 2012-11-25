import math

class point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

def pointDifference(p1,p2):
    return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)


if __name__ == "__main__" :
    p1 = point()
    p2 = point(3,4)
    
    print "Difference between p1 and p2 is : "+ repr(pointDifference(p1, p2))
