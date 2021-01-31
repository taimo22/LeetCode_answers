#674. Longest Continuous Increasing Subsequence
#https://leetcode.com/problems/longest-continuous-increasing-subsequence/submissions/
#my ans(passed)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        dp = [1] * (len(nums) + 1)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
        return max(dp)





