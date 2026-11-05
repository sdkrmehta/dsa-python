class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        def depth(node, go_left):
            d = 0
            while node:
                node = node.left if go_left else node.right
                d += 1
            return d

        left = depth(root, True)
        right = depth(root, False)
        if left == right:
            return (1 << left) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)