
#438. Find All Anagrams in a String
#https://leetcode.com/problems/find-all-anagrams-in-a-string/solution/
#my ans(passed)
from collections import *
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        s_count = defaultdict(int)
        ans = []
        start = 0
        for i in range(len(s)):

            if s_count == count:
                ans.append(start)
            if s[i] not in count:
                s_count = defaultdict(int)
                start = i + 1
                continue

            s_count[s[i]] += 1
            if count[s[i]] < s_count[s[i]]:
                while count[s[i]] < s_count[s[i]]:
                    s_count[s[start]] -= 1
                    if s_count[s[start]] == 0:
                        del s_count[s[start]]
                    start += 1

        if s_count == count:
            ans.append(start)
        return ans