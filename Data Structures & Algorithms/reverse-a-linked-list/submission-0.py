# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        if not cur:
            return cur
        nex = head.next

        if not nex:
            return cur

        while cur:
            cur.next = prev
            prev = cur
            cur = nex
            if nex:
                nex = nex.next
        return prev
            