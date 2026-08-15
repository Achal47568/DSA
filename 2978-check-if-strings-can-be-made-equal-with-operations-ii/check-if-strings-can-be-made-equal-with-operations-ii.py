class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = Counter(s1[::2])
        even2 = Counter(s2[::2])

        odd1 = Counter(s1[1::2])
        odd2 = Counter(s2[1::2])

        if even1 != even2:
            return False

        if odd1 != odd2:
            return False

        return True



  # return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
