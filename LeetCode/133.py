"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        queue = deque([node])
        clones = {str(node.val) : Node(node.val, None)}

        while queue:
            currentNode = queue.popleft()
            clonedNode = clones[str(currentNode.val)]

            for ngbr in currentNode.neighbors:
                if str(ngbr.val) not in clones:
                    clones[str(ngbr.val)] = Node(ngbr.val, [])
                    queue.append(ngbr)

                clonedNode.neighbors.append(clones[str(ngbr.val)])

        return clones[str(node.val)]