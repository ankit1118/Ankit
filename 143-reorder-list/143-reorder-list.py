# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        q = []
        while head:
            q.append(head)
            head = head.next
        p = dummy = ListNode(0)

        while len(q)>1:
            h = q.pop(0)
            t = q.pop()
            p.next = h
            h.next = t
            p = t
            p.next = None
        
        if q: 
            p.next = q.pop()
            p = p.next
            p.next = None
        
        return dummy.next
        """
        Do not return anything, modify head in-place instead.
        """