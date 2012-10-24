import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def estimate_pi():
    """
    compute 1/pi
    """
    result = 0
    k = 0
    while True:
        loopVal =( (2 * math.sqrt(2) / 9801 )* (factorial(4*k) * (1103 + 26390*k)) )/ (factorial(k)**4 * 396**(4*k))
        result += loopVal  
        if abs(loopVal) < 1e-15: break
        k =k+1

    return 1 / result

print estimate_pi()