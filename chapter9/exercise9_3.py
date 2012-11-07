
file_path = "../resource/words.txt"

def avoids(word, forbiddenLetters):
    for letter in word:
        if letter in forbiddenLetters:
            return False
    return True


print avoids("foo","bar")
print avoids("foo","bor")

def findWordsNotInForbiddenList():
    forbiddenLetters = raw_input("Enter forbidden Letters >")
    
    fin = open(file_path)
    words_found = 0
    for lines in fin:
        word = lines.strip()
        if avoids(word,forbiddenLetters):
            print word
            words_found = words_found+1
    print """ Numer of letters no in """,forbiddenLetters," are :",words_found
            
            

findWordsNotInForbiddenList()