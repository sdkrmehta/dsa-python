from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:

        queue = deque([root])
        ans = root.val

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

            ans = queue[-1].val if queue else ans

        return ans