class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, target):
    if root == None:
        return None

    curr = root

    while curr.val != None:
        if curr == target:
            return curr
        elif target < curr.val:
            curr = curr.left
        else:
            curr = curr.right

    return None