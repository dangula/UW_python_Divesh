word1 = "noon"
word2 = "moon"

print word1[:]
print word1[::-1]

print word2[:]
print word2[::-1]

def is_palindrome(word):
    if word[:]==word[::-1]:
        return True
    else:
        return False
    

print is_palindrome(word1)
print is_palindrome(word2)
print is_palindrome("madam")
print is_palindrome("123432")