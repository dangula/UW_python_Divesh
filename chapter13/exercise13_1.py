import string

file_path = "../resource/sampleFile.txt"

def make_word_list():
    words = list()
    fin = open(file_path)
    for line in fin:
        Lineword = line.split()
        for word in Lineword:
            words.append(stripWords(word))
    return words

def stripWords(word):
    import string
    word =  word.lower()
    word = word.translate(None,string.punctuation+string.whitespace)
    
    return word

if __name__ =='__main__':
    print make_word_list()

