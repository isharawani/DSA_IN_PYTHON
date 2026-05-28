#Problem 167: Two Sum II – Input Array Is Sorted
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l +=1
            else:
                return [l+1 , r+1]
        return[]
        
#Problem 125: Valid Palindrome
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
    
#Problem 26: Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l=0
        for r in range(1,len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l+1
    
#Problem 27: Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        for r in range (len(nums)):
            if nums[r] !=val:
                nums[l]=nums[r]
                l += 1
        return l
    
#Problem 75: Sort Colors (Dutch National Flag)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r=0,len(nums)-1
        i=0
        def swap(i,j):
            tmp=nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        while i <= r:
            if nums[i]== 0:
                swap(l,i)
                l += 1
            elif nums[i] == 2:
                swap(i,r)
                r -= 1
                i -= 1
            i +=1

#Problem 11: Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        l,r=0,len(height)-1
        while l<r:
            area=(r-l)*min(height[l],height[r])
            res=max(res,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res        
    
#Problem 283: Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l +=1
        return nums
        
        #Do not return anything, modify nums in-place instead.
