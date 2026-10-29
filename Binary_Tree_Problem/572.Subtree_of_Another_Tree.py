class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def check(self, root, subRoot):
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False

        if root.val != subRoot.val:
            return False

        return (
            self.check(root.left, subRoot.left)
            and self.check(root.right, subRoot.right)
        )

    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True

        if root is None:
            return False

        if self.check(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )