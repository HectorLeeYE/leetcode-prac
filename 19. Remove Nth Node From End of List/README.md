# 19. Remove Nth Node From End of List

### Difficulty: Medium

## Description
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 
Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


Example 2:


Input: head = [1], n = 1
Output: []


Example 3:


Input: head = [1,2], n = 1
Output: [1]


 
Constraints:


	The number of nodes in the list is sz.
	1 <= sz <= 30
	0 <= Node.val <= 100
	1 <= n <= sz


 
Follow up: Could you do this in one pass?

## Submission Details
- **Status**: Accepted
- **Runtime**: 4
- **Memory**: 19360000
- **Language**: python3

## Code
```python3
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

            
```
