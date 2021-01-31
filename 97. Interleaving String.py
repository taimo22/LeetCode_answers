#97. Interleaving String
#https://leetcode.com/problems/interleaving-string/
#my ans(passed)
from functools import lru_cache
class Solution:
    def isInterleave(self, S1: str, S2: str, S3: str) -> bool:
        @lru_cache(None)
        def rec(s1, s2, s3):
            if s3 == len(S3) and s2 == len(S2) and s1 == len(S1):
                return True
            if s3 > len(S3) - 1:
                return False
            res = False
            if s1 < len(S1) and S1[s1] == S3[s3]:
                res = res or rec(s1 + 1, s2, s3 + 1)

            if s2 < len(S2) and S2[s2] == S3[s3]:
                res = res or rec(s1, s2 + 1, s3 + 1)
            return res

        return rec(0, 0, 0)