import time

file_path = "../resource/words.txt"

def make_word_list():
    t = list()
    fin = open(file_path)
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def is_reverse(word1,word2):
    return word1[:]==word2[::-1]

def findAllReverseWords(wordList):
    count = 0
    i=0
    for i in range(len(wordList)-1):
        for j in range(i+1,len(wordList)-1):
            if is_reverse(wordList[i], wordList[j]):
                count +=1
                print "words %s and %s are reverse words"%(wordList[i],wordList[j])
                break
    return count


if __name__ == "__main__":
    wordList = make_word_list()
    startTime = time.time()
    count = findAllReverseWords(wordList)
    elapsed_time = time.time() - startTime
    
    print "%d reverse words found in %f seconds" %(count,elapsed_time)
    


    