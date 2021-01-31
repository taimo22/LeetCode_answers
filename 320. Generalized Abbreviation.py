#320. Generalized Abbreviation
#https://leetcode.com/problems/generalized-abbreviation/solution/
#my ans (passed)
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:

        res = []

        def rec(i, k, curr):
            if i == len(word):
                curr_copy = curr.copy()
                if k != 0:
                    curr_copy.append(f"{k}")
                res.append("".join(curr_copy))
            else:

                rec(i + 1, k + 1, curr)

                if k != 0: curr.append(f"{k}")
                curr.append(word[i])
                rec(i + 1, 0, curr)
                if curr:
                    curr.pop()
                if k != 0:
                    curr.pop()

        rec(0, 0, [])
        return res