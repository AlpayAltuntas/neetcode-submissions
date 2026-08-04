class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        return (
            abs(l - r) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def getHeight(self, node):
        if node is None:
            return 0
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))