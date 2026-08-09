class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n

        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        rightproduct = 1

        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * rightproduct

            rightproduct = rightproduct * nums[i]
        return ans  
"""
n = len(nums)
ans = []
for i in range(n):
    product = 1

    for j in range(n):
        if i != j:
            product = product * nums[j]
    ans.append(product)

return ans
"""