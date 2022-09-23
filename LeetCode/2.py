# Definition for singly-linked list.
from typing import final


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        firstNumberMultiplier = 1
        l1Copy = l1.copy()
        while l1Copy.next:
            firstNumberMultiplier *= 10
            l1Copy = l1Copy.next

        secondNumberMultiplier = 1
        l2Copy = l2.copy()
        while l2Copy.next:
            secondNumberMultiplier *= 10
            l2Copy = l2Copy.next


        finalValue = 0

        while l1.next:
            finalValue += l1.val * firstNumberMultiplier
            l1 = l1.next
            firstNumberMultiplier /= 10

        finalValue += l1.val

        while l2.next:
            finalValue += l2.val * secondNumberMultiplier
            l2 = l2.next
            secondNumberMultiplier /= 10

        finalValue += l2.val
        
        print(finalValue)


l1 = [2,4,3]
l2 = [5,6,4]

solution = Solution()

solution.addTwoNumbers(l1, l2)
        


