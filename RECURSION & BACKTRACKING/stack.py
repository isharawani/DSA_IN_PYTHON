#lc-20 VALID PARENTHESES
from ast import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={")":"(","]":"[","}":"{"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    

#lc-496 NEXT GREATER ELEMENT I
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx={n:i for i , n in enumerate(nums1)}
        res=[-1] * len(nums1)
        stack=[]
        for i in range(len(nums2)):
            cur=nums2[i]
            while stack and cur > stack[-1]:
                val=stack.pop()
                idx=nums1Idx[val]
                res[idx]=cur
            if cur in nums1Idx:
                stack.append(cur)
        return res
    

#lc-739 DAILY TEMPERATURES
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0] * len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT , stackInd =stack.pop()
                res[stackInd]=(i-stackInd)
            stack.append([t,i])
        return res
    
    
#lc-150 EVALUATE REVERSE POLISH NOTATION
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
                                                                #      t     operation    stack
        for t in tokens:                                        #    –––––   –––––––––    ––––––––– 
            if t not in '/+-*':                                 #      4                    [4]
                stack.append(int(t))                            #     13                    [4,13]
                                                                #      5                    [4,13,5]
            else:                                               #      /     13 / 5 = 2     [4,2]
                num = stack.pop()                               #      +      4 + 2 = 6     [6]
                if   t == '+': stack[-1]+=  num
                elif t == '-': stack[-1]-=  num
                elif t == '*': stack[-1]*=  num
                else         : stack[-1]= int(stack[-1]/num)    

        return stack[0]
    
        
#lc-84 LARGEST RECT IN HISTOGRAM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack= [] #pair: (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index , height = stack.pop()
                maxArea = max(maxArea , height * (i - index))
                start = index
            stack.append((start, h))
        for i , h in stack:
            maxArea = max(maxArea , h * (len(heights) - i))
        return maxArea
    
    
#lc-155 MINSTACK
class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]


    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()