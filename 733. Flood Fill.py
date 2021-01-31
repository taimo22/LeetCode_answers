#733. Flood Fill
#https://leetcode.com/problems/flood-fill/
#my ans (passed)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(now_x, now_y, newColor, chengedColor):
            if image[now_x][now_y]==newColor or image[now_x][now_y]!=chengedColor:
                return
            image[now_x][now_y]=newColor
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (now_x+x<len(image) and now_x+x>=0) and (now_y+y<len(image[0]) and now_y+y>=0):
                    dfs(now_x+x, now_y+y, newColor, chengedColor)
                else:
                    continue
        dfs(sr, sc, newColor, image[sr][sc])
        return image
