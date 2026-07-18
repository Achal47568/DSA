class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False

        bucket = {}
        size = valueDiff + 1

        for i, num in enumerate(nums):
            b = num // size

            if b in bucket:
                return True

            if b - 1 in bucket and abs(num - bucket[b - 1]) <= valueDiff:
                return True

            if b + 1 in bucket and abs(num - bucket[b + 1]) <= valueDiff:
                return True

            bucket[b] = num

            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // size]

        return False