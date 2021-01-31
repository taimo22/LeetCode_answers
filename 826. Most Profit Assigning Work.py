#826. Most Profit Assigning Work
#https://leetcode.com/problems/most-profit-assigning-work/
#my ans(but the excution takes a long time)
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        difficulty, profit = zip(*sorted(zip(difficulty, profit)))

        ans = 0
        for i in range(len(worker)):
            limit = bisect_right(difficulty, worker[i])
            if limit > 0:
                ans += max(profit[:limit])
        return ans