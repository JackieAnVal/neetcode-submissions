# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestPath(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = 1 + self.longestPath(node.left)
        right = 1 + self.longestPath(node.right)
        return max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.longestPath(root.left)
        right = self.longestPath(root.right)

        if abs(left - right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
