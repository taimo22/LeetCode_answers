#112. Path Sum
#https://leetcode.com/problems/path-sum/solution/
#my ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack = []
        if root is not None:
            stack.append((root.val, root))
        while stack != []:
            current_sum, root = stack.pop()
            if root is not None and (root.right is None) and (root.left is None) and (current_sum==sum):
                    return True
            if root is not None:
                stack.append((current_sum + getattr(root.left, "val", 0), root.left))
                stack.append((current_sum + getattr(root.right, "val", 0), root.right))
        return False


