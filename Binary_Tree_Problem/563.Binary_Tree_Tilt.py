class Solution:
    def findTilt(self, root):
        self.total_tilt = 0

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            self.total_tilt += abs(left_sum - right_sum)

            return node.val + left_sum + right_sum

        dfs(root)

        return self.total_tilt