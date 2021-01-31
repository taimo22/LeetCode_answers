#107. Binary Tree Level Order Traversal II
#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/solution/
# my ans(passed)
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        res = [[root.val]]
        while queue:
            size = len(queue)
            curr = []
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    curr.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    curr.append(node.right.val)
            if curr:
                res.append(curr)

        return res[::-1]

