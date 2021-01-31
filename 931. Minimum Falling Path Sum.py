#931. Minimum Falling Path Sum
#https://leetcode.com/problems/minimum-falling-path-sum/
#my ans(passed)
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        memo = {}

        def rec(x, y):
            if x == len(A):
                return 0
            if (x, y) in memo:
                return memo[(x, y)]
            a = rec(x + 1, y)
            b = rec(x + 1, y + 1) if y < len(A[0]) - 1 else float("inf")
            c = rec(x + 1, y - 1) if y > 0 else float("inf")
            memo[(x, y)] = A[x][y] + min(a, b, c)
            return memo[(x, y)]

        min_num = math.inf
        for i in range(len(A[0])):
            min_num = min(rec(0, i), min_num)

        return min_num