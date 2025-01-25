'''This is a program for checking if a number is palindrom or not'''

def palindrome(n):
    rev = 0
    temp = n
    
    while temp != 0:
        rem = temp % 10
        rev = rev * 10 + rem
        temp = temp // 10
    return rev == n


if __name__ == "__main__":
    n = int(input("Enter your palindrome: "))
    print(palindrome(n))