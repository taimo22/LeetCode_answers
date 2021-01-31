#287. Find the Duplicate Number
#https://leetcode.com/problems/find-the-duplicate-number/submissions/
#my ans(passed)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for n in nums:
            if bisect_right(nums, n) - bisect_left(nums, n) >= 2:
                return n
