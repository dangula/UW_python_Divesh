

def cumulativeSumOfList(origList):
    """
    Function that takes a list and return a new list where ith position is 
    the cumulative sum of original list till ith position
    """
    cSumList = list()
    i =1
    for i in range(len(origList)):
        cSumList.append(sum(origList[0:i+1]))    
    return cSumList
k =[1,2,3]
l = cumulativeSumOfList(k)

print "original list = ",k,"\nCumulative Sum = ", l

k1 =[3,5,7,9]
l1 = cumulativeSumOfList(k1)

print "original List = ",k1,"\nCumulative Sum = ", l1


k2 =[1,2,3,4,5,6,7,8,9,10]
l2 = cumulativeSumOfList(k2)

print "original List= ",k2,"\nCumulative Sum = ", l2


        

    
