#797. All Paths From Source to Target
#https://leetcode.com/problems/all-paths-from-source-to-target/solution/
# my ans(passed)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        def dfs(now_pos, node, currPath):
            if len(graph) - 1 == now_pos:
                paths.append(currPath.copy())
                return
            for p in node:
                currPath.append(p)
                dfs(p, graph[p], currPath)
                currPath.pop()

        dfs(0, graph[0], [0])

        return paths