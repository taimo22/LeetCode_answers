#763. Partition Labels
#https://leetcode.com/problems/partition-labels/
#my ans (passed)
class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        l = 0
        r = 0
        S = list(S)
        seen = {}
        ans = []

        while r < len(S) and l < len(S):

            if S[r] not in seen:
                seen[S[r]] = True

            if S[r] not in set(S[r + 1:]):
                del seen[S[r]]
                if not seen:
                    ans.append(r - l + 1)
                    l = r + 1
            r += 1

        return ans
