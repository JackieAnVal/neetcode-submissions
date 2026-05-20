# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValue(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr and curr.left: 
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #Find the the node to delete
        if not root:
            return None

        if root.val < key: 
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            #Find the smallest value from the subtree to replace it and then delete it
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minVal = self.minValue(root.right)
                root.val = minVal.val
                root.right = self.deleteNode(root.right, minVal.val)
        return root

