class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):   #extract unique elements first
            if nums[i] != 0:
                nums[k] = nums[i]
                k+=1
        while k<len(nums):   # in remaining length fill zero
            nums[k] = 0
            k += 1