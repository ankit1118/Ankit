# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return True
        elif head != None and head.next == None:
            return True
        else:
            fast = head
            slow = head
            stack = []
            while fast != None and fast.next != None:
                stack.append(slow.val)
                slow = slow.next
                fast = fast.next.next

            #madam    
            if fast != None:
                slow = slow.next

            while slow != None:
                if slow.val != stack.pop():
                    return False
                else:
                    slow = slow.next

            return True