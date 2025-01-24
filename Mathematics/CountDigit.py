'''This is program to count the number of digits in a number'''

def countDigit(n):
    count = 0
    while (n > 0):
        n = n//10
        count=count+1
    return count

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(countDigit(n))