'''This is to find to the factorial of a number'''

def factorial(n):

# using loop
    fact = 1
    if (n == 0 or n == 1):
        return 1
    for i in range(2,n+1):
        fact = fact * i
    return fact
#using recursion
    if (n == 0):
        return 1
    return n * factorial(n -1)
    

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(factorial(n))