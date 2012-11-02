def find(word,letter):
    """
    This function returns the index of given letter in a word
    """
    index = 0
    while index<len(word):
            if word[index]==letter:
                return index
            index=index+1
    return -1

print find("banana","n")

print find("banana","c")

def find(word,letter,start):
    """
    This function returns the index from give letter in a word after
    specified position
    """
    while start<len(word):
        if word[start]==letter:
            return start
        start = start+1
    return -1
        

print find("banana","n",3)

print find("banana","c",3)  

print find("banana","n",-3)
