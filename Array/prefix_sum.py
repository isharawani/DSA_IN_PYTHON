#lc-303 RANGE SUM QUERY-IMMUTABLE
from rpds import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.num=[0]*(len(nums)+1)
        for i in range(0,len(nums)):
            self.num[i+1]=self.num[i]+nums[i]        

    def sumRange(self, left: int, right: int) -> int:
        return self.num[right+1]-self.num[left]
        

#lc-560 SUBARRAY SUM EQUALS K
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        count=0
        prefixsum={0:1}
        for n in nums:
            prefix += n
            if  prefix-k in prefixsum:
                count += prefixsum[prefix-k]
            prefixsum[prefix]=prefixsum.get(prefix,0)+1
        return count


#lc-724 FIND PIVOT INDEX
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftsum=0
        for i in range(len(nums)):
            rightsum=total-nums[i]-leftsum
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return-1


#lc-523 CONTINUOUS ARRAY
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder={0:-1}
        prefix=0
        for i , n in enumerate(nums):
            prefix += n
            r=prefix % k
            if r not in remainder:
                remainder[r]=i
            elif i-remainder[r]>1:
                return True
        return False


#lc-238 PRODUCT OF ARRAY EXCEPT SELF
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*(len(nums))
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]

        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res


#lc-930 BINARY SUBARRAY SUMS
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pri={0:1}
        res=0
        summ=0
        for i in nums:
            summ+=i
            res+=pri.get(summ-goal,0)
            pri[summ]=pri.get(summ,0)+1
        return res


#lc-410 SPLIT ARRAY LARGEST SUM
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
            from typing import List

class Solution:

    def splitArray(self, nums: List[int], k: int) -> int:

        left = max(nums)
        right = sum(nums)

        while left < right:

            mid = (left + right) // 2

            if self.canSplit(nums, k, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def canSplit(self, nums, k, maxSum):

        subarrays = 1
        currentSum = 0

        for num in nums:

            if currentSum + num > maxSum:
                subarrays += 1
                currentSum = 0

            currentSum += num

        return subarrays <= k