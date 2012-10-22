
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

c= gcd(52,13)

print c