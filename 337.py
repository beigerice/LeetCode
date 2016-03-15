class Solution(object):
    def dfs(self, node):
        if not node:
            return (0,0)
        lc = self.dfs(node.left)
        rc = self.dfs(node.right)
        return (max(lc)+max(rc),node.val+lc[0]+rc[0])
    def rob(self, root):
        return max(self.dfs(root))
