# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, r: Optional[TreeNode]) -> int:
        return 0 if not r else max(self.maxDepth(r.left), self.maxDepth(r.right)) + 1
