#609. Find Duplicate File in System
#https://leetcode.com/problems/find-duplicate-file-in-system/solution/
#my ans (passed)
import re
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        data=defaultdict(list)
        for i in range(len(paths)):
            p=paths[i].split(" ")
            for j in range(1, len(p)):
                content=re.search(r"(\()(.*?)\)",p[j]).group(0)
                data[content].append(p[0]+"/"+re.sub("\(.+?\)", "", p[j]))
        res=[]
        for v in data.values():
            if len(v)>1:
                res.append(v)
        return res