from numpy.dual import eig

file_path = "../resource/words.txt"

def make_word_list():
    t = list()
    fin = open(file_path)
    for line in fin:
        word = line.strip()
        t.append(word)
    return t
def convertStringToTuple(word):
    wList = list(word)
    wList.sort()
    wTuple = tuple(wList)
    return wTuple

def annagramDict(words):
    anngram_dict = dict()
    for word in words:
        tWord = convertStringToTuple(word)
        anngram_dict[tWord] = anngram_dict.setdefault(tWord,[])+[word]
    return anngram_dict
 
def filter_length(d, n):
    res = dict()
    for word, anagrams in d.iteritems():
        if len(word) == n:
            res[word] = anagrams
    return res   


if __name__ == '__main__':
    wordList = make_word_list()
    annagram_Dict = annagramDict(wordList)
    i =0
    for words in wordList:
        key = convertStringToTuple(words)
        annagrams = annagram_Dict[key]
        if len(annagrams)>1:
            #print annagrams
            i += 1
    print " %d annagram lists found" %i
    
    
    t = []
    for v in annagram_Dict.values():
        if len(v) > 1:
            t.append((len(v), v))

    t.sort(reverse = True)
    
    #print t
    
    eightLetters = filter_length(annagram_Dict, 8)
    
    print eightLetters