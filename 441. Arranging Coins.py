#441. Arranging Coins
#https://leetcode.com/problems/arranging-coins/
#my ans(passed)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        total = [1]
        i = 2
        while total[-1] < n:
            total.append((1 * i) + total[-1])
            i += 1

        return bisect_right(total, n)