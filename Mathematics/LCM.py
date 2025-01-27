#naive method
# def lcm(a,b):
    # res = max(a,b)
    # while True:
    #     if res % a == 0 and res % b == 0:
    #         return res
    #     res = res + 1
    # return res

# efficient method
def gcd(a,b):
    
    if b == 0 :
        return a
    return gcd(b, a % b)
    
def lcm(a,b) :
    return a * b // gcd(a,b)

a = 12
b = 13
print(lcm(a,b))