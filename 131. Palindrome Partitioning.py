#131. Palindrome Partitioning
#https://leetcode.com/problems/palindrome-partitioning/solution/
#my ans(passed)
def check_palin(s):
    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            return False
    return True
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def rec(start, s, currentList):
            if start >= len(s):
                result.append(currentList.copy())
                return
            for end in range(start, len(s)):
                if check_palin(s[start:end + 1]):
                    currentList.append(s[start:end + 1])
                    rec(end + 1, s, currentList)
                    currentList.pop()

        result = []
        rec(0, s, [])
        return result

