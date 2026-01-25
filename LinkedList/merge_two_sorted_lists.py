from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Intuition - 
# The following variables are needed, p1 and p2 for the two lists
# ans for the start of the merged list
# ptr for the current node of the merged list


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        p1, p2 = list1, list2

        # Determine head
        if p1.val <= p2.val:
            ans = p1
            p1 = p1.next
        else:
            ans = p2
            p2 = p2.next

        ptr = ans

        while p1 and p2:
            if p1.val <= p2.val:
                ptr.next = p1
                p1 = p1.next
            else:
                ptr.next = p2
                p2 = p2.next
            ptr = ptr.next

        ptr.next = p1 or p2
        return ans
