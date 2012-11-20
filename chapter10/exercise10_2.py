
def chop(Origlist):
    """
    This fuction takes a list and remove first and last element 
    """
    del Origlist[0]
    del Origlist[len(list)-1]
    
    
list1 = [1,2,3,4,5]
print list1
chop(list1)
print list1


def middle(Origlist):
    """
    This functon takes a list and returns the a new list that 
    contains all but first and last element of the origial list
    """
    return Origlist[1:len(list)-1]

list2 = [1,2,3,4,5,6,7,8]
list3 = middle(list2)

print list2
print list3