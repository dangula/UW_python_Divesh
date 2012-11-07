
def has_palindrome(i, start, End):
    s = str(i)[start:start+End]
    return s[::-1] == s
    
def check(i):
    if has_palindrome(i, 2, 4) and has_palindrome(i+1, 1, 5) and has_palindrome(i+2, 1, 4) and has_palindrome(i+3, 0, 6) :
        return True
    else:
        return False
    

def check_all():
    i=100000
    while i<999999:
        if check(i):
            print i
        i=i+1

check_all()

    
    