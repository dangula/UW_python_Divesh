import copy

class point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
class rectangle(point):
    def __init__(self,height=0,width=0,x=0,y=0):
        self.height = height
        self.width = width
        self.corner = point(x,y)

def move_rectangle(rect,dx,dy):
    rect.corner.x = rect.corner.x+dx
    rect.corner.y = rect.corner.y+dy

def move_rectangle_Copy(rect,dx,dy):
    newRect = copy.copy(rect)
    newRect.corner.x +=dx
    newRect.corner.y +=dy
    return newRect

def move_rectangle_deepCopy(rect,dx,dy):
    newRect = copy.deepcopy(rect)
    newRect.corner.x +=dx
    newRect.corner.y +=dy
    return newRect
    
    
def print_rectangle(rect):
    print "rectangle height is %g and width is %g with corner(%g,%g)" % (rect.height,rect.width,rect.corner.x,rect.corner.y)
    

if __name__ == "__main__":
    rect1 =  rectangle(50,100,1,2)
    print "rect1=",print_rectangle(rect1)
    print "perform move_rectangle"
    move_rectangle(rect1, 2, 1)
    print"rect1 = ",
    print_rectangle(rect1)  
    print "perform move_rectangle_copy"
    rect2 = move_rectangle_Copy(rect1, 1, 1)
    print"rect1 = ",
    print_rectangle(rect1)
    print"rect2 = ",
    print_rectangle(rect2)
    print "perform move_rectangle_deepcopy"
    rect3 = move_rectangle_deepCopy(rect1, 1, 1)
    print"rect1 = ",
    print_rectangle(rect1)
    print"rect3 = ",
    print_rectangle(rect3)