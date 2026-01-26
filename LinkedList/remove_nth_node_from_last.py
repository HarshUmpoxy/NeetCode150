# Intuition - 
# The following variables are needed, fast and slow for the two pointers
# At first we place the fast pointer n steps ahead of the slow pointer
# Then we move both pointers until fast reaches the end

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # If fast is None, we remove the head
        if not fast:
            return head.next

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return head