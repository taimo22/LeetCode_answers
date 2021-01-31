#64. Minimum Path Sum
#https://leetcode.com/problems/minimum-path-sum/
#my ans(passeed)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        num_of_way=[[0]*(len(grid[0])) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                down = grid[i][j]+num_of_way[i-1][j] if j==0 else num_of_way[i][j-1]+grid[i][j]
                right = grid[i][j]+num_of_way[i][j-1] if i == 0 else num_of_way[i-1][j]+grid[i][j]
                num_of_way[i][j] = min(down, right)
        return num_of_way[len(grid)-1][len(grid[0])-1]

