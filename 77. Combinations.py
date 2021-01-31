#77. Combinations
#https://leetcode.com/problems/combinations/
#my ans(passed)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def rec(ind, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return

            for i in range(ind + 1, n + 1):
                curr.append(i)
                rec(i, curr)
                curr.pop()

        rec(0, [])
        return res