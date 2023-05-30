# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach
# Slow pointer
# Fast pointer
# When fast pointer arrives at the end, return slow pointer!

# 1 1
# 2 3
# 3 5
# 4 7

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowPointer = head
        fastPointer = head

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next


        return slowPointer