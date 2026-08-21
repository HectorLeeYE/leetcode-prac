# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        new_list_head = new_list

        while list1 and list2:
            if (list1.val < list2.val):
                # curr_1 is smaller so it should be added first
                new_list_head.next = list1
                list1 = list1.next      # Advance pointer of list1
            else:
                # curr_1 is greater
                new_list_head.next = list2
                list2 = list2.next
            
            new_list_head = new_list_head.next
        
        if list1:
            new_list_head.next = list1
        else:
            new_list_head.next = list2
    
        return new_list.next
