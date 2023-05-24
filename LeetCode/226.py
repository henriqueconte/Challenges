# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            
        return root

solution = Solution()
tree = TreeNode(4, 
                            TreeNode(2, 
                                    TreeNode(1), 
                                    TreeNode(3)
                                    ),
                            TreeNode(7,
                                    TreeNode(6),
                                    TreeNode(9)
                                    )
                            )
solution.print_tree(tree)
print()
solution.invertTree(tree)
solution.print_tree(tree)
            
            
