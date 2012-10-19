def do_twice(f):
    f()
    f()
def do_four(f):
    do_twice(f)
    do_twice(f)

def plusLine():
    print '+','-'*4,
    
def printMainLine():
    do_twice(plusLine)
    print '+'

    
def halfMidLine():
    print '|',' '*4, 

def oneMidLine():
    do_twice(halfMidLine)
    print '|'

def printMidLines():
    do_four(oneMidLine)

def OneHalf():
    printMainLine()
    printMidLines()
    
def printGrid():
    do_twice(OneHalf)
    printMainLine()
    
printGrid()   
    
    