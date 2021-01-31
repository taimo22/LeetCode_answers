#113. Path Sum II
#https://leetcode.com/problems/path-sum-ii/solution/
#my ans(passed)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        def rec(root, path):
            if root:
                path.append(root.val)
                if (not root.left and not root.right) and (len(path) > 0) and (sum_ == sum(path)):
                    paths.append(path)
                else:
                    rec(root.left, path.copy())
                    rec(root.right, path.copy())

        paths = []
        rec(root, [])
        return paths

