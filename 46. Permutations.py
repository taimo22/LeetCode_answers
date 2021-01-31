#46. Permutations
#https://leetcode.com/problems/permutations/
#my ans(passed)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * (len(nums))
        res = []

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if not visited[i]:
                    curr.append(nums[i])
                    visited[i] = True
                    backtrack(curr)
                    curr.pop()
                    visited[i] = False

        backtrack([])
        return res
