from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if root == None:
            return 0

        ans = 0
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                if node.left.left == None and node.left.right == None:
                    ans += node.left.val
                else:
                    queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return ans