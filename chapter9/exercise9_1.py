
file_path = "../resource/words.txt"

fin = open(file_path)

for lines in fin:
    word = lines.strip()
    if len(word)>20:
        print word
        
