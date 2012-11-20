import string

def is_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    str1List = list(str1.lower())
    str1List.sort()
    str2List = list(str2.lower())
    str2List.sort()
    
    return str1List == str2List


if __name__ == '__main__':
    def test_is_anagram(word1,word2):
        result = is_anagram(word1, word2)
        if result:
            print " strings %s and %s are anagrams" %(word1,word2)
        else:
            print " strings %s and %s are not anagrams" %( word1 , word2 )
    
    test_is_anagram("tops", "pots")
    test_is_anagram("No", "on")
    test_is_anagram("moon", "noon")

   
    