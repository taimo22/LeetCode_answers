#253. Meeting Rooms II
#https://leetcode.com/problems/meeting-rooms-ii/
#my ans(passed)
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key= lambda x: x[0])
        h = []
        heapq.heappush(h, intervals[0][1])

        for i in range(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if s < h[0]:
                heapq.heappush(h, e)
            else:
                heapq.heappushpop(h, e)

        return len(h)
