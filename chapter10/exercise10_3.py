
def is_sorted1(OrigList):
    i = 0
    while i< len(OrigList)-1:
        if OrigList[i]>OrigList[i+1]:
            return False
        i +=1
    return True 

def is_sorted2(OrigList):
    SortedList = sorted(OrigList)
    return OrigList == SortedList




if __name__ == "__main__":
    k1 =[1,1,1,2,3,3,3,4,4,4,5,100] 
    print "Given list ",k1," sorted = ",is_sorted1(k1)   
    print "Given list ",k1," sorted = ",is_sorted2(k1)
    k2 =[1,1,1,2,5,5,5,0,0,0,4,4,4] 
    print "Given list ",k2," sorted = ",is_sorted1(k2)   
    print "Given list ",k2," sorted = ",is_sorted2(k2)  

