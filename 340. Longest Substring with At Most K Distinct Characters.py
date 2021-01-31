#340. Longest Substring with At Most K Distinct Characters
#https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
#my ans(passed)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        i = 0
        j = 0
        ans = 0
        n = len(s)
        seen = {}
        while i < n and j < n:

            if len(seen) == k and s[j] not in seen:
                seen[s[j]] = j
                char, ind = min(seen.items(), key=lambda x: x[1])
                i = ind + 1
                seen.pop(char)
            else:
                seen[s[j]] = j
                j += 1
                ans = max(ans, j - i)
        return ans