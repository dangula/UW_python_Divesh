
def is_power(a,b):
    """
    this function takes 2 numbers a and b and returns True if a can be expressed as a b to the power of some 
    """
    if a<=0|b<=1:
        return False #a and b cannot be negative and b should negative and b should be greater than 1, because 1 cannot be power of any other integer
    if a==1:
        return True
    if a%b==0:
        if a==b|a==1:
            return True
    else:
        return False
    return is_power(a/b, b)

print is_power(9, 3)