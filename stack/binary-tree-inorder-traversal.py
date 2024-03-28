# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # initialize "queue-like" structure
        q = []

        # base case
        if root is None: return []

        # recursive function
        def inOrder(node):
            if node is None: return []

            # recursively call left and right
            inOrder(node.left)
            q.append(node.val)
            inOrder(node.right)

        inOrder(root)
        return q
