class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def check(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        if not self.check(p.left, q.left):
            return False

        if not self.check(p.right, q.right):
            return False

        return True

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        return self.check(p, q)