# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    visitedNodes = []
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        while head.next:
            self.visitedNodes.append(head)
            head = head.next
            if head in self.visitedNodes:
                return True

        return False