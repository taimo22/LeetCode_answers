#187. Repeated DNA Sequences
#https://leetcode.com/problems/repeated-dna-sequences/
#my ans(passed)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashmap = defaultdict(int)
        for i in range(9, len(s)):

            if i >= 9:
                hashmap[s[i - 9:i + 1]] += 1

        ans = []
        for k, v in hashmap.items():
            if v > 1:
                ans.append(k)
        return ans


