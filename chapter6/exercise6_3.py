

def is_greaterThanOrEquals(x,y):
    if x<=y:
        return True
    else:
        return False
    
def in_detween(x,y,z):
         if is_greaterThanOrEquals(x, y) and is_greaterThanOrEquals(y, z):
             return True
         else:
             return False
         
print in_detween(1, 2, 0)