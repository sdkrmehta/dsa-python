def __init__(self):
        self.ans = 0

def averageOfSubtree(self, root):
    self.dfs(root)
    return self.ans

def dfs(self, node):
    if node is None:
        return [0, 0]

    left = self.dfs(node.left)
    right = self.dfs(node.right)

    total_sum = left[0] + right[0] + node.val
    count = left[1] + right[1] + 1

    if node.val == total_sum // count:
        self.ans += 1

    return [total_sum, count]