import time

file_path = "../resource/words.txt"

def make_word_list():
    t = list()
    fin = open(file_path)
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def binarySearch(SearchList, searchValue, left, right):
                if right < left:
                        return -1
                mid = (left + right) / 2
                if searchValue > SearchList[mid]:
                        return binarySearch(SearchList, searchValue, mid + 1, right)
                elif searchValue < SearchList[mid]:
                        return binarySearch(SearchList, searchValue, left, mid - 1)
                else:
                        return mid
                    
def FormatSearchResult(searchWord,foundIndex,TimeElapsed):
    if foundIndex != -1:
        print "Word %s found at index %d in time %f seconds" %(searchWord,foundIndex,TimeElapsed)
    else:
        print "Word %s not found time taken %f seconds" %(searchWord,TimeElapsed)

 
 
if __name__ == '__main__':
        a = [1, 2, 3, 5, 9, 11, 15, 66]
        start_time1 = time.time()
        index1 =  binarySearch(a, 5,0,len(a)-1)
        elapsed_time1= time.time() - start_time1
        FormatSearchResult("a", index1, elapsed_time1)
        
        start_time2 = time.time()
        wordList = make_word_list()
        index2 =  binarySearch(wordList, "bing",0, len(wordList)-1)
        elapsed_time2 = time.time() - start_time2
        FormatSearchResult("bing", index2, elapsed_time2)
        
        start_time3 = time.time()
        wordList = make_word_list()
        index3 = binarySearch(wordList, "em",0, len(wordList)-1)
        elapsed_time3 = time.time() - start_time3
        FormatSearchResult("em",index3,elapsed_time3)
        
        start_time4 = time.time()
        wordList = make_word_list()
        index4 =  binarySearch(wordList, "queue",0, len(wordList)-1)
        elapsed_time4 = time.time() - start_time4
        FormatSearchResult("queue", index4, elapsed_time4)
        
        start_time5 = time.time()
        wordList = make_word_list()
        index5 = binarySearch(wordList, "fake",0, len(wordList)-1)
        elapsed_time5 = time.time() - start_time5
        FormatSearchResult("fake",index5,elapsed_time5)
        
        start_time6 = time.time()
        wordList = make_word_list()
        index6= binarySearch(wordList, "foo",0, len(wordList)-1)
        elapsed_time6 = time.time() - start_time6
        FormatSearchResult("foo",index6,elapsed_time6)
        
        
        
        
        
        
        
        
        