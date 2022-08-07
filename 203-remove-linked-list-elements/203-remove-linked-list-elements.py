# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        arr = []
        newList = head
        newListHead = head
        while head != None:
            if head.val != val:            
                arr.append(head.val)
            head = head.next
            
        for i in range(len(arr)):
            newList.val = arr[i]
            if(i == len(arr) - 1):
                newList.next = None
            else:
                newList = newList.next
        if len(arr) == 0:
            newListHead = None
        return newListHead