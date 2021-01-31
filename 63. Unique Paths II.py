#63. Unique Paths II
#https://leetcode.com/problems/unique-paths-ii/
#my ans(passed)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        self.end = [len(obstacleGrid), len(obstacleGrid[0])]
        memo = {}

        def dfs(x, y):
            if obstacleGrid[x][y] == 1:
                return 0
            if x == self.end[0] - 1 and y == self.end[1] - 1:
                return 1

            if (x, y) in memo:
                return memo[(x, y)]
            down = 0
            if x < self.end[0] - 1:
                down = dfs(x + 1, y)

            right = 0
            if y < self.end[1] - 1:
                right = dfs(x, y + 1)

            memo[(x, y)] = down + right
            return memo[(x, y)]

        return dfs(0, 0)


