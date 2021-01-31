#993. Cousins in Binary Tree
#https://leetcode.com/problems/cousins-in-binary-tree/solution/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        leaves = {x: None, y: None}
        queue = deque([(root, 0, None)])
        while queue:
            size = len(queue)
            for _ in range(size):
                node, depth, parent = queue.popleft()
                if node.val == x or node.val == y:
                    leaves[node.val] = [depth, parent]
                    if leaves[x] and leaves[y]:
                        break
                if node.left:
                    queue.append((node.left, depth + 1, node.val))
                if node.right:
                    queue.append((node.right, depth + 1, node.val))

        return (leaves[x][0] == leaves[y][0] and leaves[x][1] != leaves[y][1])
