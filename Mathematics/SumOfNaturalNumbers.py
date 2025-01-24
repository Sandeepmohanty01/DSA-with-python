''' This is a program for 
printing the sum of n 
natural numbers'''

def sumOfNaturalNumber(n):
    return n*(n+1)//2

if __name__ == "__main__":
    n = int(input("Enter the number till which you want the sum to be printed: "))
    print(sumOfNaturalNumber(n))