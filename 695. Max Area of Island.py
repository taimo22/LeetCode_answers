#695. Max Area of Island
#https://leetcode.com/problems/max-area-of-island/
#my ans(passed)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_num = 0

        def dfs(x, y):
            grid[x][y] = "E"
            res = 0
            for r, c in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                next_r, next_c = r + x, c + y
                if next_r >= 0 and next_r < len(grid) and next_c >= 0 and next_c < len(grid[0]) and grid[next_r][
                    next_c] == 1:
                    res += dfs(next_r, next_c) + 1
            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_num = max(max_num, dfs(i, j) + 1)
        return max_num