#938. Range Sum of BST
#https://leetcode.com/problems/range-sum-of-bst/
#my ans (passed) dfs
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total = 0
        def dfs(node, low, high):
            nonlocal total
            if not node:
                return 0
            elif low <= node.val <= high:
                total += node.val
            left = dfs(node.left, low, high)
            right = dfs(node.right, low, high)
            return
        dfs(root, low, high)
        return total
#my ans (passed) bfs
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total=0
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if low<=node.val<=high:total+=node.val
            if node.right:queue.append(node.right)
            if node.left:queue.append(node.left)
        return total
#version 2
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total=0
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if low<=node.val<=high:total+=node.val
            if node.right and high>node.val :queue.append(node.right)
            if node.left and low<node.val :queue.append(node.left)
        return total

