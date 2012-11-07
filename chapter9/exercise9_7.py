
file_path = "../resource/words.txt"

def three_consecutive_double(word):
    count = 0
    i = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count+1
            if count == 3:
                return True
            i=i+2
        else:
            count =0
            i=i+1
    return False

fin = open(file_path)

print """ Triple douple words in file are : """
for lines in fin:
    word = lines.strip()
    if three_consecutive_double(word):
            print word
            

