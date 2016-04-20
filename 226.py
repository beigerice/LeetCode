class Solution:
    def invertTree(self, root):
        if root:
            if root.left != None:
                root.left, root.right = root.right, root.left
                self.invertTree(root.left)
                self.invertTree(root.right)
            else:
                if root.right != None:
                    root.left, root.right = root.right, root.left
                    self.invertTree(root.left)
                else:
                    return root
            return root
            
