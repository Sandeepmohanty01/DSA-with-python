'''Given two numbers a and b, find the sum of a and b. 
Since the sum can be very large, 
find the sum modulo 10^9+7.'''


# Input:
# a = 9223372036854775807
# b = 9223372036854775807
# Output: 582344006
# Explanation: 
# 9223372036854775807 + 9223372036854775807 
# = 18446744073709551614.
# 18446744073709551614 mod (109+7)
# = 582344006

# Input:
# a = 1000000007
# b = 1000000007
# Output: 0
# Explanation: 1000000007 + 1000000007 =
# (2000000014) mod (109+7) = 0

#User function Template for python3

class Solution:
    def sumUnderModulo(self,a,b):
        # code here
        sum = a+b
        return sum %((10**9)+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a,b = map(int,input().strip().split())
        ob=Solution()
        print(ob.sumUnderModulo(a,b))

        print("~")
# } Driver Code Ends