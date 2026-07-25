# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # one item fast and one item slow
        # fast incr by 2
        # slow incr by 1
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: return True
        return False

        