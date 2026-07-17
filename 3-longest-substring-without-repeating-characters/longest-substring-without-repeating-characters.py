class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            if s[right] in d and d[s[right]] >= left: #check for repeat
                left = d[s[right]]+1 #moves left pointer 
            d[s[right]] = right
            ans = max(ans,right-left+1)
        return ans