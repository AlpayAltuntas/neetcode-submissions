class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, low, high):
            if not node:
                return True

            # Node must be inside the allowed range
            if node.val <= low or node.val >= high:
                return False

            # Left side must be smaller
            # Right side must be larger
            return (
                validate(node.left, low, node.val)
                and validate(node.right, node.val, high)
            )

        return validate(root, float("-inf"), float("inf"))
