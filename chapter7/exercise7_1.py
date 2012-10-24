#===============================================================================
# def print_n(s, n):
#    if n <= 0:
#        return
#    print s
#    print_n(s, n-1)
#===============================================================================


def print_n(s,n):
    """
    function to print s, n times
    """
    while(n>0):
        print s
        n= n-1


print_n("test",5)

