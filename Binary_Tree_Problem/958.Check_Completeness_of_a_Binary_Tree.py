from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        queue = deque([root])
        past = False

        while queue:
            node = queue.popleft()
            if node == None:
                past = True
            else:
                if past == True:
                    return False
                else:
                    queue.append(node.left)
                    queue.append(node.right)

        return True