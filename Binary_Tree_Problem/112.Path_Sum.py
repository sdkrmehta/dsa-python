class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        def dfs(node, total):
            if node == None:
                return False

            total += node.val

            if node.left == None and node.right == None:
                return total == targetSum

            return dfs(node.left, total) or dfs(node.right, total)

        return dfs(root, 0)