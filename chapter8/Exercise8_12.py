
UpperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"


def shiftLetters(caseType,letter,n):
    """
    This function takes a letter and shifts it by n places
    """
    origIndex = caseType.index(letter)
    shiftedIndex = origIndex+n
    return caseType[shiftedIndex%26]


def rotate_word(word,n):
    """
     This Function takes a word and shifts each letter in the word by n places
    """
    Rotated_word = ""
    for letters in word:
        if letters.isupper():
            Rotated_word = Rotated_word+shiftLetters(UpperCaseLetters, letters, n)
        elif letters.islower():
            Rotated_word = Rotated_word+shiftLetters(LowerCaseLetters, letters, n)
        else:
            Rotated_word=Rotated_word+letters       
    return Rotated_word



print rotate_word("2Cheer", 7)   
print rotate_word("MeLon!!!", -10)