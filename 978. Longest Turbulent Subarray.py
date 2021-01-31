#978. Longest Turbulent Subarray
#https://leetcode.com/problems/longest-turbulent-subarray/
#my ans(passed)
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        i = 0
        j = 0
        n = len(arr)
        sign = 1
        ans = 1
        while j < n - 1:
            print(f"i: {i}, j: {j}, ans: {ans}")
            if sign * arr[j] < sign * arr[j + 1]:
                j += 1
            else:
                i = j + 1
                j += 1
            ans = max(ans, j - i + 1)
            sign *= -1

        i = 0
        j = 0
        sign = 1
        while j < n - 1:
            print(f"i: {i}, j: {j}, ans: {ans}")
            if sign * arr[j] > sign * arr[j + 1]:
                j += 1
            else:
                i = j + 1
                j += 1
            ans = max(ans, j - i + 1)
            sign *= -1

        return ans