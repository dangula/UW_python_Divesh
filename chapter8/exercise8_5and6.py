
def countLetterOccurance(word,letter):
    """
    This function returns the number of times a given letter is present in a word
    if the letter is not present then 0 is returned
    """
    count = 0
    for letters in word:
        if letters == letter:
            count = count +1
    return count

print countLetterOccurance("Mississippi", "s")
print countLetterOccurance("Mississippi", "e")

def countLetterOccurance(word,letter,start):
    """
    This function returns the number of times a given letter is present in a word
    if the letter is not present then 0 is returned
    """
    count = 0
    while start<len(word):
        if word[start] == letter:
            count = count +1
        start=start+1
    return count

print countLetterOccurance("Mississippi", "s",4)
print countLetterOccurance("Mississippi", "e",4)