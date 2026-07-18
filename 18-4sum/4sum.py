class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()

                for k in range(j + 1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])

                    if fourth in seen:
                        ans.add((nums[i], nums[j], fourth, nums[k]))

                    seen.add(nums[k])

        return [list(x) for x in ans]