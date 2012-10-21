

def is_triangle(a,b,c):
    """
    Check in sides of lenght a,b and c can form a triangle or not
    prints 'YES' if the sides can form  a triangle
    prints 'NO' if the sides cannot form a triangle
    """
    if a+b>c:
        if b+c>a:
            if c+a>b:
                print "YES"        
            else :
                print "NO"
        else:
            print "NO"          
    else :
        print "NO"
        

is_triangle(3, 10, 11)

def is_triangle_interactive():
    a = raw_input("Enter a integer for 'a' :")
    b = raw_input("Enter a integer for 'b' :")
    c = raw_input("Enter a integer for 'c' :")
    
    is_triangle(int(a),int(b),int(c))
    

is_triangle_interactive()
        
        
