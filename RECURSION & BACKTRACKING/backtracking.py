#Subsets — LC 78

from ast import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            #decision  not to include nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
#Permutations — LC 46
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        #base case
        if (len(nums)==1):
            return[nums.copy()]

        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result
#combination sum lc-39
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        comb=[]
        def dfs(i,total):
            if total==target:
                res.append(comb.copy())
                return
            if i>=len(candidates) or total>target:
                return
            #decision to include candidates[i]
            comb.append(candidates[i])
            dfs(i,total+candidates[i])
            #decision not to include candidates[i]
            comb.pop()
            dfs(i+1,total)
        dfs(0,0)
        return res

#lc-131 palindrome partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]
        def dfs(i):
            if i>= len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.isPali(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
    def isPali(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r=l+1,r-1
        return True
    
#lc-79 word search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS=len(board),len(board[0])
        path=set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r<0 or c<0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c]or
                (r,c) in path):
                return False
            path.add((r,c))
            res=(dfs(r+1,c,i+1)or
                 dfs(r-1,c,i+1)or
                 dfs(r,c+1,i+1)or
                 dfs(r,c-1,i+1))
            path.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):return True
        return False
        O(n*m*4^n)
#lc-22 Generate parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def backtrack(openN,closedN):
            if openN==closedN==n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1 ,closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN ,closedN + 1)
                stack.pop()
        backtrack(0,0)
        return res
#lc-90 Subsets II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtrack(i,subset):
            if i == len(nums):
                res.append(subset[::])
                return
            #all subset that include nums[i]
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()
            #all subset that not include nums[i]
            while i+1 < len(nums) and nums[i]== nums[i+1]:
                i += 1
            backtrack( i+1,subset)
        backtrack(0,[])
        return res
