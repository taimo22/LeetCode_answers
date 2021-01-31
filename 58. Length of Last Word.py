class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")

        while len(s) > 0 and s[-1] == "":
            s.pop()
        return len(s[-1]) if s else 0

