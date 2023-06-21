# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels_dict = {}
        ans = []
        self.dfs(root, 0, levels_dict)
        for level in levels_dict:
            ans.append(levels_dict[level][-1])

        return ans

    def dfs(self, root, level, levels_dict):
        if root:
            str_level = str(level)
            if str_level in levels_dict:
                levels_dict[str_level].append(root.val)
            else:
                levels_dict[str_level] = [root.val]

            self.dfs(root.left, level + 1, levels_dict)
            self.dfs(root.right, level + 1, levels_dict)
