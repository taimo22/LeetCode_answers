#819. Most Common Word
#https://leetcode.com/problems/most-common-word/
#my ans(passed)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.replace(",", " ").split(" ")
        count=defaultdict(int)
        for i in range(len(paragraph)):
            para=(paragraph[i][:-1] if not(paragraph[i].isalpha()) else paragraph[i]).lower()
            if para not in set(banned) and para!="":
                    count[para]+=1
        return max(count, key=count.get)