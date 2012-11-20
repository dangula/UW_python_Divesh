def sumall ( *t ):
    """This function calculates the sum of all of its arguments"""
    s = 0
    for i in range(len(t)) :
        s += t[i]
    return s

if __name__ == "__main__" :

   print  sumall ( 1,2,3,4,5,6,7,8,9,10)
   print  sumall ( 5.235,5,8.90,54 )
   print  sumall ( ) 
   print  sumall ( 5 )
   #print  sumall ( 'a','b','c','d' ) 