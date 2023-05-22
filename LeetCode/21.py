# Definition for singly-linked list.
import copy

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
    def append(self, new_val):
        if self.val == None:
            self.val = new_val
            return

        list_copy = self

        while (list_copy.next != None):
            list_copy = list_copy.next

        list_copy.next = ListNode(new_val, None)
        


class Solution:
    def mergeTwoLists(self, list1, list2):
        final_list = ListNode()

        while(list1.next != None and list2.next != None):
            if list1.val <= list2.val:
                final_list.append(list1.val)
                list1 = list1.next
            else:
                final_list.append(list2.val)
                list2 = list2.next

        while(list1.next != None):
            final_list.append(list1.val)
            list1 = list1.next

        while(list2.next != None):
            final_list.append(list2.val)
            list2 = list2.next

        while(final_list.next != None):
            print(final_list.val)
            final_list = final_list.next

        return final_list

    

solution = Solution()
print(solution.mergeTwoLists([], []))
print(solution.mergeTwoLists([1,2,4], [1,3,4]))