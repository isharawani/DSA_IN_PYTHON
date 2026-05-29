#PROBLEM 509: Factorial
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fib(n-1)+self.fib(n-2)
    
#PROBLEM 2: Fibonacci Number
from typing import List
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fib(n-1)+self.fib(n-2)
        
#PROBLEM 344: Sum of Array (Recursive)
def reverseString(s):
    if len(s) <= 1:
        return s
    return reverseString(s[1:]) + s[0]

#PROBLEM 125: Check Palindrome Recursively
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l<r and not self.alphaNum(s[l]):
                l += 1
            while r>l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1

        return True

    def alphaNum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
#PROBLEM 704: Binary Search (Recursive)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]> target:
                r=m-1
            elif nums[m]< target:
                l=m+1
            else:
                return m
        return -1
        
#PROBLEM 231: Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
       return n > 0 and (n & (n-1)) == 0
       