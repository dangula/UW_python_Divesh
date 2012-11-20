
def histogram(s):
    d = dict()
    for c in s:
        count =  d.get(c,0)
        d[c] = count+1
    return d
        
def most_Freqent(word):
    d = histogram(word)
    t = []
    for key in d.keys() :
        t.append ( (d[key], key) )
    t.sort(reverse = True)
    r = []
    for c in t :
        r.append( (c[1],c[0] ) )
    return r

if __name__ == '__main__':
    word = 'maki kirikiri'
    print most_Freqent(word)