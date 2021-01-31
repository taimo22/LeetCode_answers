#349. Intersection of Two Arrays
#https://leetcode.com/problems/intersection-of-two-arrays/solution/
#my ans(passed)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def bs(nums, target):
            l = 0
            r = len(nums) - 1
            nums = sorted(nums)
            while l <= r:
                mid = (r + l) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        if len(nums1) >= len(nums2):
            long_ar = nums1
            short_ar = nums2
        else:
            long_ar = nums2
            short_ar = nums1
        ans = []
        for n in short_ar:
            if bs(long_ar, n) and n not in set(ans):
                ans.append(n)
        return ans
