class Solution:
    def mySqrt(self, x: int) -> int:
        low, high, ans = 1,x,0
        while low <= high:
            mid = (low + high)//2    # // -> returns quotient

            if mid<= x // mid:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

