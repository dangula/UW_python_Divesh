import random

def has_duplicates(OrigList):
    SortedList = sorted(OrigList)
    i = 0
    while i< len(SortedList)-1:
        if SortedList[i]==SortedList[i+1]:
            return True
        i +=1
    return False

def random_bdays(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(students, samplesSize):
    count = 0
    for i in range(samplesSize):
        t = random_bdays(students)
        if has_duplicates(t):
            count += 1
    return count

if __name__ == "__main__":
    def test_has_duplicates(OrgList):
        if(has_duplicates(OrgList)):
            print "list ",OrgList,"has duplicates"
        else:
            print "list ",OrgList,"has no duplicates"
    
    list1 = [1,2,3,4,5,5,3,2]
    list2 = [10,5,3,4,7,2,8,1]
    list3 = [1,2,3,"one","two","an"]
    list4 = [1,2,3,"one","two","an",3]
    
    test_has_duplicates(list1)
    test_has_duplicates(list2)
    test_has_duplicates(list3)
    test_has_duplicates(list4)
    
    print "No of dupe bdays from class of 23 students, sampled 1000 times is :", count_matches(23, 1000)
    print "No of dupe bdays from class of 23 students, sampled 5000 times is :", count_matches(23, 5000)
    print "No of dupe bdays from class of 50 students, sampled 1000 times is :", count_matches(50, 1000)
    print "No of dupe bdays from class of 100 students, sampled 1500 times is :", count_matches(100, 1500)
    


