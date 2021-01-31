#694. Number of Distinct Islands
#https://leetcode.com/problems/number-of-distinct-islands/
#my ans (passed)
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        total = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    shape = {(i - i, j - j)}
                    top_left = (i, j)
                    while stack:
                        x, y = stack.pop()
                        grid[x][y] = "#"
                        for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            next_r, next_c = x + r, y + c
                            if 0 <= next_r < n and 0 <= next_c < m and grid[next_r][next_c] == 1:
                                stack.append((next_r, next_c))
                                shape.add((next_r - top_left[0], next_c - top_left[1]))

                    total.add(frozenset(shape))

        return len(total)

