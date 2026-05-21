# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            height = 1 + max(left[1], right[1])
            #In Python, comparing a boolean to == True is redundant.
            #Instead of: left[0] and right[0] == True Use: left[0] and right[0]
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <=1
            return [balanced, height]
        return dfs(root)[0]
    
           
    """def longestPath(self, node: Optional[TreeNode]) -> int:
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
            return False"""
