class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        new_s = ""

        for ch in s:
            if ch.isalnum():
                new_s += ch

        return new_s == new_s[::-1]

'''
if ch.isalnum():

isalnum() checks whether the character is:

a letter → True
a number → True
space → False
comma → False
! → False

'''