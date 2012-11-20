import time

file_path = "../resource/words.txt"

def make_word_dict():
    wordDict = dict()
    fin = open(file_path)
    for line in fin:
        word = line.strip()
        wordDict[word] = word[0]
    return wordDict


if __name__ == "__main__":
    wordDict = make_word_dict()
    
    start_time =  time.time()
    print time.time(),"bing" in wordDict,time.time(),
    print start_time - time.time()
    
    start_time1 =  time.time()
    print time.time(),"queue" in wordDict,time.time(),
    print start_time1 - time.time()
    
    
    