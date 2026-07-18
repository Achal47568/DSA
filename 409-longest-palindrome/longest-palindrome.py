class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        ans = 0

        for ch in s:
            if ch in seen:
                ans += 2
                seen.remove(ch)
            else:
                seen.add(ch)

        if seen:
            ans += 1

        return ans