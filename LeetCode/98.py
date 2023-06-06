# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))
    

    def dfs(self, root, minLeft, maxRight):
        if not root:
            return True

        if root.val > minLeft and root.val < maxRight:
            return self.dfs(root.left, minLeft, root.val) and self.dfs(root.right,root.val, maxRight)
        else:
            return False 