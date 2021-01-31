#4. Median of Two Sorted Arrays
#https://leetcode.com/problems/median-of-two-sorted-arrays/solution/
#my answer
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        mid = []
        while i < len(nums1) and j < len(nums2):

            if nums1[i] <= nums2[j]:
                mid.append(nums1[i])
                i += 1
            else:
                mid.append(nums2[j])
                j += 1


        if len(nums1) >= i:
            mid += nums1[i:]
        if len(nums2) >= j:
            mid += nums2[j:]



        return (mid[len(mid) // 2 - 1] + mid[len(mid) // 2]) / 2 if len(mid) % 2 == 0 else float(mid[len(mid) // 2])
