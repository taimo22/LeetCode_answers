#347. Top K Frequent Elements
#https://leetcode.com/problems/top-k-frequent-elements/solution/
#my ans (passed)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        count = Counter(nums)
        heap = []
        for key, v in count.items():
            heap.append((-v, key))

        heapq.heapify(heap)
        ans = []
        while k:
            frq, key = heapq.heappop(heap)
            ans.append(key)
            k -= 1
        return ans
