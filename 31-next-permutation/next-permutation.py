class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2

        # Find the first decreasing number
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Find a number bigger than nums[i]
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the remaining part
        nums[i + 1:] = reversed(nums[i + 1:])