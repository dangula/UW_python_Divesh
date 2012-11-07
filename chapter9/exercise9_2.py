file_path = "../resource/words.txt"

def has_no_e(word):
    for letter in word:
        if letter in 'e' or letter in'E':
            return False
    return True

print has_no_e("abe")    
print has_no_e("eab")    
print has_no_e("aeb")    
print has_no_e("abc")    


fin = open(file_path)

total_word_count = 0
words_with_e = 0
for lines in fin:
    total_word_count=total_word_count+1
    word = lines.strip()
    if has_no_e(word):
        print word
        words_with_e=words_with_e+1

percent_no_e = (words_with_e*100)/total_word_count

print """percent of words with no "e" is """,percent_no_e,"%"
        

        