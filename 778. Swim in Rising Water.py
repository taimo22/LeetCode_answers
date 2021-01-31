#778. Swim in Rising Water
#https://leetcode.com/problems/swim-in-rising-water/
#my ans(passed)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        m = len(grid[0])
        n = len(grid)
        t_mat = [[math.inf] * m for _ in range(n)]
        t_mat[0][0] = grid[0][0]

        stack = [(0, 0)]
        while stack:
            x, y = stack.pop()

            for r, c in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
                next_r, next_c = r + x, y + c
                if 0 <= next_r < n and 0 <= next_c < m:
                    t = max(t_mat[x][y], grid[next_r][next_c])
                    if t_mat[next_r][next_c] > t:
                        t_mat[next_r][next_c] = t
                        stack.append((next_r, next_c))

        return t_mat[n - 1][m - 1]

