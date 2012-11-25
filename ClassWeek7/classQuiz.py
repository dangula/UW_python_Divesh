
class c(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "x = %g and y = %g" %(self.x,self.y)
    
    def __repr__(self):
        return repr("x = %g and y = %g" %(self.x,self.y))
    


if __name__ == "__main__":
    instC = c(5,4)
    print instC
    print instC.x
    print instC.y
    print str(instC)
    print repr(instC)
    print str(instC) == repr(instC)