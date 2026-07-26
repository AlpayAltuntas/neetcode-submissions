class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # 1. Find end of first half (slow/fast pointers)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 2. Reverse the second half and cut it off
        second = slow.next
        slow.next = None
        prev = None
        while second:
            second.next, prev, second = prev, second, second.next
        # 3. Merge the two halves, alternating
        first, second = head, prev
        while second:
            first.next, first = second, first.next
            second.next, second = first, second.next