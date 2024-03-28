# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # base case: no tree
        if root is None:
            return 0

        # base case: no children
        if root.left is None and root.right is None:
            return 1
        
        # set up heights of both subtrees
        left, right = 99999, 99999
        if root.left:
            left = self.minDepth(root.left)
        if root.right:
            right = self.minDepth(root.right)

        return min(left, right) + 1


