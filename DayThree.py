# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        new_head = None
        s = None
        
        while l1 is not None and l2 is not None:
            # compare values 
            if l1.val < l2.val:
                # set the first item of the list to the new list
                if new_head is None:
                    new_head = l1
                    # move the s pointer as head of the list
                    s = new_head
                else:
                    # set the s to point to list 1  as the next list
                    s.next = l1
                    # move the s pointer to the next item in list
                    s = s.next
                # move l1 to next item in list
                l1 = l1.next
            # similar    
            else:
                if new_head is None:
                    new_head = l2
                    s = new_head
                else:
                    s.next = l2
                    s = s.next
                l2 = l2.next
        return new_head