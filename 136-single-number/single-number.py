class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s.pop()   #removes and return remaining elements

"""
# can be done using XOR function:  
XOR rules: a^a = 0  , a^0 = a

example: 4^1^2^1^2
         4^(1^1)^(2^2)
         4^0^0
         4

code 1 : 

ans = 0
for num in nums:
    ans ^= num
return ans

"""
"""
code 2:  return list({x for x in nums if nims.count(x) == 1})[0]
code 3:  return next(iter(set(nums)))   # only works when all the duplicates are removed

"""
