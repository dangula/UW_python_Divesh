def do_twice(f,string):
    f(string)
    f(string)

def print_spam(string):
    print string
    print string
def do_four(f,string):
    do_twice(f,string)
    do_twice(f,string)
    
do_twice(print_spam,"spam")  

print "output from do 4"

do_four(print_spam,"spam")
    