# The first solution is to store the nodes in an array and use simple logic to reorder the list

# Intuition - 
# The following variables are needed, slow and fast for the two pointers
# prev for the previous node of the second half
# tmp for the next node of the first half
# tmp2 for the next node of the second half

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now, we will reverse the linked list from slow+1 (slow.next) till the end
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
