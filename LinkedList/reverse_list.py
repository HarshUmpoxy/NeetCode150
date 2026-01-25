# Intuition - after some dry run and observation, we can see that we need to reverse the links of the nodes
# We actually need three pointers instead of the usual two in the first try of solution
# And atlast, we fix the pointer of p2 to p1 since loop ends

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        p1 = None; p2 = head; p3 = head.next
        while p2.next != None:
            p2.next = p1
            p1 = p2
            p2 = p3
            p3 = p3.next
        p2.next = p1 # important visualization
        return p2