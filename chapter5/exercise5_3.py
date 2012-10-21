

def check_fermat(a,b,c,n):
    if a**n+b**n == c**n:
        if n == 2:
            print "n has to greater than 2 for Fermat's theorem"
        else:
            print "Holly Smoke, Fermat was wrong"
            
    else :
        print "No, that does't work"
                    
        

check_fermat(4, 3, 5, 4)

def check_fermat_interactive():
    a = raw_input("Enter a integer for 'a' :")
    b = raw_input("Enter a integer for 'b' :")
    c = raw_input("Enter a integer for 'c' :")
    n = raw_input("Enter a integer for 'n' :")
    
    check_fermat(int(a), int(b), int(c), int(n))
    
check_fermat_interactive()