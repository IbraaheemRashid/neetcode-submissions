# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # store the curr
        # make next next point to next
        # make the next point to curr
        # until next becomes null
        prev = None
        temp = head

        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        
        return prev