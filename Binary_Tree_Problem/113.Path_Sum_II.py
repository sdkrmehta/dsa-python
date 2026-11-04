class Solution:
    def pathSum(self, root, targetSum):
        ans = []

        def dfs(node, total, path):
            if node == None:
                return

            total += node.val
            path.append(node.val)

            if node.left == None and node.right == None:
                if total == targetSum:
                    ans.append(path.copy())

            else:
                dfs(node.left, total, path)
                dfs(node.right, total, path)

            path.pop()

        dfs(root, 0, [])
        return ans