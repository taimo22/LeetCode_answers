#784. Letter Case Permutation
#https://leetcode.com/problems/letter-case-permutation/
#my ans(passed)
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        S = S.lower()
        res = []

        def rec(i, curr):

            if i == len(S):
                res.append("".join(curr.copy()))

            else:
                if S[i] in string.ascii_lowercase:
                    curr.append(S[i].upper())
                    rec(i + 1, curr)
                    curr.pop()
                curr.append(S[i])
                rec(i + 1, curr)
                curr.pop()

        rec(0, [])
        return res
