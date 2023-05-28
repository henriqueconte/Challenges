# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftHeight = self.getSubTreeHeight(root.left)
        rightHeight = self.getSubTreeHeight(root.right)
        if abs(leftHeight - rightHeight) > 1:
            return False
        leftSide = self.isBalanced(root.left)
        rightSide = self.isBalanced(root.right)

        return leftSide and rightSide

    def getSubTreeHeight(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.getSubTreeHeight(root.left), self.getSubTreeHeight(root.right))

        