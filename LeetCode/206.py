# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        lastNode = ListNode(head.val)
        while head.next:
            head = head.next
            currentNode = ListNode(head.val)
            currentNode.next = lastNode
            lastNode = currentNode
            
        return lastNode

# 1, 2, 3, 4, 5
# 2, 1, 3, 4, 5
# 2, 3, 1, 4, 5
# 2, 3, 4, 1, 5
# 2, 3, 4, 5, 1