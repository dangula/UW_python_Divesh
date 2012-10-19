

def repeat_lyric():
    print_lyric()
    print_lyric()
    
def print_lyric():
    print "foo"
    print "bar"


def print_twice(bruce):
    print bruce;
    print bruce

def cat_twice(part1,part2):
    cat = part1+part2
    print_twice(cat)
    
line1 = "bing twiddle"
line2 = "twiddle bang"

cat_twice(line1, line2)


result = print_twice("cat")

print result