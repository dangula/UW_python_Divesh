import math

def hypotenuse(x,y):
    """
    hypotenuse function takes to sides of a triangle and returns the hypotenuse
    """
    # print x**2+y**2
    result = math.sqrt(x**2+y**2)
    #return 0.0
    return result

print hypotenuse(1,1)