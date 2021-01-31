#1658. Minimum Operations to Reduce X to Zero
#https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

#my ans(time limit exceeded)
import math
from functools import lru_cache
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        @lru_cache(None)
        def rec(r, l, x):
            print(f"rec({r}, {l}, {x})")
            if x == 0:
                return 0
            if l > r or x < 0:
                return math.inf

            right = rec(r - 1, l, x - nums[r]) + 1
            left = rec(r, l + 1, x - nums[l]) + 1
            return min(right, left)

        res = rec(len(nums) - 1, 0, x)
        return -1 if res == math.inf else res


#my ans(passed)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        r = 0
        l = 0
        total = sum(nums)
        maxi = -1
        current = 0

        while r < len(nums):

            current += nums[r]
            while l <= r and current > total - x:
                current -= nums[l]
                l += 1
            if current == total - x:
                maxi = max(maxi, r - l + 1)
            r += 1

        return len(nums) - maxi if maxi != -1 else maxi
