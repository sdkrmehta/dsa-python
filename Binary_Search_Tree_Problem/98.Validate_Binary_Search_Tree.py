class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def check(self, root, minn, maxx):
        if root is None:
            return True
        
        if root.val < minn or root.val > maxx:
            return False
        
        checkLeft = self.check(root.left, minn, root.val - 1)
        checkRight = self.check(root.right, root.val + 1, maxx)

        return checkLeft and checkRight

    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.check(root, -100000000000000000000, 100000000000000000000)