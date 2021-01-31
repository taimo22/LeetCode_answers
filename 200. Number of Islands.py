#200. Number of Islands
#https://leetcode.com/problems/number-of-islands/
#my ans (passed) dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ROWS=len(grid)
        self.COLS=len(grid[0])
        def dfs(row, col):
            grid[row][col]="E"
            for ro, co in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if row+ro >= 0 and row+ro < self.ROWS and col+co >= 0 and col+co < self.COLS and grid[row+ro][col+co]=="1":
                    dfs(row+ro, col+co)
        count=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1":
                    dfs(row, col)
                    count+=1
        return count
#after improvement
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid==None or len(grid)==0: return 0
        self.ROWS=len(grid)
        self.COLS=len(grid[0])
        def dfs(r, c):
            if r<0 or c<0 or r>=self.ROWS or c>=self.COLS or grid[r][c]=="0":
                return
            grid[r][c]="0"
            for ro, co in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r+ro, c+co)
        count=0
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if grid[r][c]=="1":
                    count+=1
                    dfs(r, c)
        return count

#my ans (passed) bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ROWS=len(grid)
        self.COLS=len(grid[0])
        count=0
        queue=deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    queue.append((r, c))
                    while queue:
                        row, col = queue.popleft()
                        if grid[row][col]=="1":
                            grid[row][col]="E"
                        elif grid[row][col]!="1":
                            continue
                        for ro, co in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            if row+ro >= 0 and row+ro < self.ROWS and col+co >= 0 and col+co < self.COLS :
                                queue.append((row+ro, col+co))
                    count+=1
        return count