#151. Reverse Words in a String
#https://leetcode.com/problems/reverse-words-in-a-string/submissions/
#my answer (passed)
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for i in reversed(s.split(" ")):
            if i == "": continue
            ans.append(i)
        return " ".join(ans)

