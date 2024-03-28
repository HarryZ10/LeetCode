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

        def dfs(node, depth, answer) -> int:

            if not node: return answer
            if not node.left and not node.right: return min(answer, depth)

            left = dfs(node.left, depth + 1, answer)
            right = dfs(node.right, depth + 1, answer)
            return min(left, right)

        return dfs(root, 1, float('inf'))


