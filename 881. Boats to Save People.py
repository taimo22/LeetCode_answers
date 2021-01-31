#881. Boats to Save People
#https://leetcode.com/problems/boats-to-save-people/
#my ans(passed)

from collections import deque
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = deque(sorted(people))
        ans = 0
        while people:
            now_pe = 0
            del_time = 0
            while del_time < 2 and people and now_pe + people[-1] <= limit:
                now_pe += people.pop()
                del_time += 1
            while del_time < 2 and people and now_pe + people[0] <= limit:
                now_pe += people.popleft()
                del_time += 1
            ans += 1

        return ans
