class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(maxSum, currentSum)

        return maxSum


"""
[-2,1,-3,4,-1,2,1,-5,4]

current = -2
maxsum = nums[0]  => -2
currentSum = max(nums[i], currentSum + nums[i])

suppose: current = -2, nums[i] = 1
therefore: nums[i] = 1
current + nums[i] = -2 + 1 = -1
max(1, -1) = 1
current = 1

iteratively find out the other numbers 

"""
"""
class Solution:
    def maxSubArray(self, nums):

        maxSum = float('-inf')
        currSum = 0

        for num in nums:
            currSum += num
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum = 0

        return maxSum

    """