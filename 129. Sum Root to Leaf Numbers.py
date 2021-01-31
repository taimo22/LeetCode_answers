#129. Sum Root to Leaf Numbers
#https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/
#my ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def rec(node, path):
            nonlocal total
            if node:

                path += str(node.val)
                if not node.left and not node.right:
                    total += int(path)
                else:
                    rec(node.left, path)
                    rec(node.right, path)

        total = 0
        rec(root, "")
        return total
