def checkPrime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count+=1
    if count > 2:        
        return False
    else:
        return True
    

n =2
print(checkPrime(n))