class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current+nums[i])
            maximum = max(maximum, current)
        return maximum

"""
nums = [-2,1,-3,4,-1,2,1,-5,4]
current = -2
maximum = -2
for i in range of numbers:
    eg : current = -2, nums[i] = 1
    therefore = nums[i] = 1, current + nums[i] = -2+1 = -1
    max(1, -1) = 1 
    therefore :current = 1
    last line to compare all values and find out the maximum

"""