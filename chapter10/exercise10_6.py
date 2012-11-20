

def remove_duplicates(origList):
    dupeLessList = list()
    
    for item in origList:
        if item not in dupeLessList:
            dupeLessList.append(item)
    
    return dupeLessList



if __name__ == "__main__":
    list1 = [1,2,3,4,1,2,3,4,1,2,3,4,5]
    print "list ",list1,"after removing dupes is",remove_duplicates(list1)
    list2 = [1,2,"one","three",[1,3],"five",2,[1,2],1,3,[1,3]]
    print "list ",list1,"after removing dupes is",remove_duplicates(list2)
