
def printStringReverse(str):
    length = len(str)
    index =-1
    for i in range(length):
        print str[index]
        index= index -1

str = raw_input("enter a String >")  
printStringReverse(str)
