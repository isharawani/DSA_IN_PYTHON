
#Problem 643: Maximum Average Subarray I
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum=maxSum=sum(nums[:k])
        for i in range(len(nums)-k):
            curSum += nums[i+k]-nums[i]
            maxSum=max(maxSum,curSum)
        return maxSum/k
    

#Problem 3: Problem 2: Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res=max(res,r - l + 1)
        return res
        

#Problem 121: Best Time to Buy and Sell Stock
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxProfit=0
        while r< len(prices):
            if prices[l] < prices[r]:
                profit=prices[r]-prices[l]
                maxProfit=max(maxProfit,profit)
            else:
                l = r
            r += 1
        return maxProfit      
    
#Problem 424: Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0

        l=0
        maxf=0
        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            maxf=max(maxf,count[s[r]])
            while ( r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res=max(res, r - l + 1)
        return res


#Problem 713: Number of Subarrays with Product < K
class Solution:
    
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res=0
        l=0
        product=1
        for r in range(len(nums)):
            product *= nums[r]
            while l <= r and product >=k:
                product =product// nums[l]
                l += 1
            res += (r - l + 1)
        return res
        
