
def printFunc(n):
    print " function call ",
    print n

def do_n(n):
    if n<=0:
        return
    else:
        printFunc(n)
        do_n(n-1)

print "Enter a number"
n = raw_input()
do_n(int(n))
    
