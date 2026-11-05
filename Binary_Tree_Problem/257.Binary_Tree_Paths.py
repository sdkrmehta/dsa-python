from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:

        if root == None:
            return []

        ans = []

        def dfs(node, path):

            path.append(str(node.val))

            # Check if leaf node
            if node.left == None and node.right == None:
                ans.append("->".join(path))
                return

            if node.left:
                dfs(node.left, path.copy())

            if node.right:
                dfs(node.right, path.copy())

        dfs(root, [])

        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.binaryTreePaths(root))

root = TreeNode(1)

print(sol.binaryTreePaths(root))