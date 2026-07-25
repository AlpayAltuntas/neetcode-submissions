# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def revList(curr, prev):
            #base case, at end of list so new head is now prev
            if curr is None:
               return prev
            
            #reverse node
            nxtNode = curr.next
            curr.next = prev

            #go to next node
            return revList(nxtNode, curr)
        return revList(head, None)