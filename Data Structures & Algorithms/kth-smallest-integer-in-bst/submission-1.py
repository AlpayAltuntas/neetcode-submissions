# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## ADD ALL NODES TO A LIST
        ## just index into the list
        res = []
        def dfs(node):
            nonlocal res
            if not node or len(res) == k: return None
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res[k-1]
