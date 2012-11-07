
# Exercise 4
def uses_only(word,letters):
    for letter in word:
        if letter not in letters:
            return False
    return True
       
    

print uses_only("aaaabbbbccccdddeee","abcdefghi")


#Exercise 5 similar to above

def uses_all(word,letters):
    return uses_only(letters, word)

print uses_all("aaaaeeewwwbbbccc","abce")

#Exercise 6
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

print is_abecedarian("ado")
print is_abecedarian("aha")