#Euclidean alogoritm
def gcd(a,b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a

#optimised Euclidean algorithm
def gcd (a,b):
    if b == 0:
        return a
    return gcd (b, a%b)

a = 10
b = 11
print(gcd(a,b))