#17. Letter Combinations of a Phone Number
#https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/
#my ans(passed)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table={"2":"abc","3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result=[]
        if digits=="":
            return result
        def rec(idx, digits, prev):
            if idx>=len(digits):return ""
            for i in table[digits[idx]]:
                rec(idx+1, digits, prev+i)
                if len(prev+i)==len(digits):
                    result.append(prev+i)
        rec(0, digits, "")
        return result
