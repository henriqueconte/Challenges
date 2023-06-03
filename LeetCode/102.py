# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    levelsDict = {}
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levelsDict = {}
        self.bfs(root, 0)
        result = [[] for i in range(len(self.levelsDict)) ]
        for level, values in self.levelsDict.items():
            result[int(level)] = values
        
        return result

    def bfs(self, root, level):
        if root:
            levelStr = str(level)
            if levelStr in self.levelsDict:
                self.levelsDict[levelStr].append(root.val)
            else:
                self.levelsDict[levelStr] = [root.val]
            self.bfs(root.left, level + 1)
            self.bfs(root.right, level + 1)