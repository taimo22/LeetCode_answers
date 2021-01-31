#841. Keys and Rooms
#https://leetcode.com/problems/keys-and-rooms/solution/
#my ans (passed)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        stack = [0]
        while stack:
            room = stack.pop()
            for nei in rooms[room]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)
        return all(visited)
