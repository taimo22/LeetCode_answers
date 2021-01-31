#568. Maximum Vacation Days
#https://leetcode.com/problems/maximum-vacation-days/
#my ans (passed)
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        self.num_of_city = len(flights)
        self.num_of_week = len(days[0])
        memo = {}

        def rec(now_city, now_week):
            if (now_city, now_week) in memo:
                return memo[(now_city, now_week)]
            if now_week == self.num_of_week:
                return 0
            max_days = float("-inf")
            for i in range(self.num_of_city):
                if i == now_city or flights[now_city][i] != 0:
                    day = days[i][now_week] + rec(i, now_week + 1)
                    if day > max_days:
                        max_days = day
            memo[(now_city, now_week)] = max_days
            return max_days
        return rec(0, 0)