# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_lowest_ancestor(root, p, q):
            if not root:
                return None

            if root == p or root == q:
                return root

            left_LA = find_lowest_ancestor(root.left, p, q)
            right_LA = find_lowest_ancestor(root.right, p, q)

            if left_LA and right_LA:
                return root
            if left_LA and not right_LA:
                return left_LA
            if not left_LA and right_LA:
                return right_LA

        lowest_ancestor = find_lowest_ancestor(root, p, q)
        return lowest_ancestor