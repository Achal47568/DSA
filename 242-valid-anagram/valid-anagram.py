class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        # return Counter(s) == Counter(t)     
        if len(s1) != len(s2):
            return False
        
        L1 = [0]*128
        L2 = [0]*128

        for i in s1:
            L1[ord(i)] +=1
        for i in s2:
            L2[ord(i)] +=1
        if L1 == L2:
            return True
        else:
            return False