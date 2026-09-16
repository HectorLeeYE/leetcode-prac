# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next        # At nth node
        
        if fast is None: #nth node at the end
            return head.next
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next        # Slow catches up to before nth node
        
        slow.next = slow.next.next

        return head

            