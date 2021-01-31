#451. Sort Characters By Frequency
#https://leetcode.com/problems/sort-characters-by-frequency/
#my ans (passed)
import heapq
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:

        count = Counter(s)
        heap = []

        for st in s:
            heap.append((-count[st], st))

        heapq.heapify(heap)
        ans = []
        while heap:
            frq, key = heapq.heappop(heap)
            ans.append(key)
        return ans
