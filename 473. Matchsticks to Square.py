#473. Matchsticks to Square
#https://leetcode.com/problems/matchsticks-to-square/solution/
#my ans(passed)
from functools import lru_cache
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
        total = sum(nums)
        one_edge = total // 4

        if one_edge * 4 != total:
            return False

        nums.sort(reverse=True)

        @lru_cache(None)
        def dfs(i, one, two, three, four):

            if i == len(nums):
                return True

            res = False
            if one + nums[i] <= one_edge:
                res = res or dfs(i + 1, one + nums[i], two, three, four)

            if two + nums[i] <= one_edge:
                res = res or dfs(i + 1, one, two + nums[i], three, four)

            if three + nums[i] <= one_edge:
                res = res or dfs(i + 1, one, two, three + nums[i], four)

            if four + nums[i] <= one_edge:
                res = res or dfs(i + 1, one, two, three, four + nums[i])

            return res

        return dfs(0, 0, 0, 0, 0)
