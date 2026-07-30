# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #brute force
        list_len = 0
        node = head
        while node:
            list_len += 1
            node = node.next

        # Target is at index (list_len - n). If that's the head, drop it.
        if n == list_len:
            return head.next

        # Walk to the node just before the target.
        prev = head
        for _ in range(list_len - n - 1):
            prev = prev.next
        prev.next = prev.next.next
        return head


        