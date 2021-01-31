#1198. Find Smallest Common Element in All Rows
#https://leetcode.com/problems/find-smallest-common-element-in-all-rows/
#my ans (passed)
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        hashmap = Counter(mat[0])

        for i in range(1, len(mat)):
            key = hashmap.keys()
            for k in set(key):
                if k not in set(mat[i]):
                    del hashmap[k]
                else:
                    hashmap[k] += 1

        return min(hashmap.keys()) if hashmap else -1

#my ans(passed)
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        for j in range(m):
            found = True
            i = 1
            while i < n and found:
                res = bisect_left(mat[i], mat[0][j])
                found = (mat[i][min(res, len(mat[0]) - 1)] == mat[0][j])
                i += 1
            if found:
                return mat[0][j]
        return -1
