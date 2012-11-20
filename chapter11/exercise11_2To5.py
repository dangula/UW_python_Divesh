
import time

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram_get(s):
    d = dict()
    for c in s:
        count =  d.get(c,0)
        d[c] = count+1
    return d

def print_hist(h):
    for c in h:
        print c, h[c]

def print_hist_alphabetical(h):
    keyList = h.keys()
    keyList.sort()
    
    for key in keyList:
        print key,h[key]
    
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def reverse_lookup_list(d,v):
    rlist = list()
    for k in d:
        if d[k] == v:
            rlist.append(k)
    return rlist

def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv

def invert_dict_getdefault(d):
    inv = dict()
    for key in d:
        val = d[key]
        d.setdefault(val,key)
    return inv
 
if __name__ == "__main__":
    
    start_time = time.time()
    hist1 = histogram("mississippi")
    print hist1, time.time() - start_time
    
    start_time1 = time.time()
    hist2 = histogram_get("abcabcabdeffeg")
    print hist1, time.time() - start_time1

    print_hist(hist2)
    print" "
    print_hist_alphabetical(hist2)
    print "reverse lookup"
    print reverse_lookup(hist2, 1)
    print reverse_lookup(hist2, 2)
    #print reverse_lookup(hist2, 3)
    #print reverse_lookup(hist2, 4)
    
    print "reverse lookup list"
    print reverse_lookup_list(hist2, 1)
    print reverse_lookup_list(hist2, 2)
    print reverse_lookup_list(hist2, 3)
    print reverse_lookup_list(hist2, 4)

    print "invert dict"
    print invert_dict(hist2)
    print "invert dict set default"
    print invert_dict(hist2)

