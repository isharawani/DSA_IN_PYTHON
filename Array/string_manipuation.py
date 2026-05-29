#Problem 125: Valid Palindrome
from ast import List
from collections import defaultdict
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
    
#Problem 344: Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        #Do not return anything, modify s in-place instead.
        def reverse(l,r):
            if l<r:
                s[l],s[r]=s[r],s[l]
                reverse(l+1,r-1)
        reverse(0,len(s)-1)

#Problem 242: Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS,countT ={},{}
        for i in range(len(s)):
            countS[s[i]]= 1+ countS.get(s[i],0)
            countT[t[i]]= 1+ countT.get(t[i],0)
        for c in countS:
            if countS[c]!= countT.get(c,0):
                return False
        return True                 

#Problem 387: First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=defaultdict(int)
        for c in s:
            count[c]+=1
        for i,c in enumerate(s):
            if count[c]==1:
                return i
        return -1
    
#Problem 438: Find All Anagrams in a String

class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter

        p_count = Counter(p)
        s_count = Counter()
        res = []
        left = 0

        for right in range(len(s)):
            s_count[s[right]] += 1

            if right - left + 1 > len(p):
                s_count[s[left]] -= 1
                if s_count[s[left]] == 0:
                    del s_count[s[left]]
                left += 1

            if s_count == p_count:
                res.append(left)

        return res


#Problem 151: Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return ' '.join(reversed(words))
    
