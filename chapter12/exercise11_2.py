import random

def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res

def sort_by_length_rand(words):
    import random
    random.seed()
    t = []
    for word in words:
       t.append((len(word),random.random(), word))

    t.sort(reverse=True)

    res = []
    for length,random, word in t:
        res.append(word)
    return res

if __name__ =='__main__':
    t=['a','rat','be','hat','it','four','five','three','divesh','two']
    print sort_by_length(t)
    print sort_by_length_rand(t)