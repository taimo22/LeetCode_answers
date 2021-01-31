#474. Ones and Zeroes
#https://leetcode.com/problems/ones-and-zeroes/
#my ans(passed)
from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        def rec(i, zeros, ones):
            if i == len(strs):
                return 0
            if (i, zeros, ones) in memo:
                return memo[(i, zeros, ones)]
            count = Counter(strs[i])
            taken = -1
            if zeros - count["0"] >= 0 and ones - count["1"] >= 0:
                taken = rec(i + 1, zeros - count["0"], ones - count["1"]) + 1
            not_taken = rec(i + 1, zeros, ones)
            memo[(i, zeros, ones)] = max(taken, not_taken)
            return memo[(i, zeros, ones)]
        return rec(0, m, n)
