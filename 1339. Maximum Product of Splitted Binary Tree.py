#1339. Maximum Product of Splitted Binary Tree
#https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
#my ans(passed, but reduntdant)
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        self.M = 10 ** 9 + 7

        def dfs(node):
            if node is None:
                return 0
            total = node.val + dfs(node.right) + dfs(node.left)

            return total

        self.total_sum = dfs(root)

        def dfs2(node):
            if node is None:
                return 0
            total = node.val + dfs2(node.right) + dfs2(node.left)
            self.max_total=max(self.max_total, (self.total_sum - total) * total)
            return total
        self.max_total = 0
        dfs2(root)
        return (self.max_total) % self.M