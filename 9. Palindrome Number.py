#9. Palindrome Number
#https://leetcode.com/problems/palindrome-number/submissions/
#my ans(passed)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[~i]:
                return False
        return True
