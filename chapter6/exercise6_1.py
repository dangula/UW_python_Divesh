
def compare(x=0,y=0):
    if x>y:
        return 1
    if x==y:
        return 0
    if x<y:
        return -1
    

print compare(4,2)
print compare(-5,0)
print compare(0,0)
print compare(1)
print compare(None,1)
print compare()