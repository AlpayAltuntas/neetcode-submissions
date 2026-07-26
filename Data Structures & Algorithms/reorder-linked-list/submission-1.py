class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: 
            return 
        # separate halfes
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second: 
            second.next,prev,second = prev, second, second.next
        first,second = head,prev
        while second:
            first.next, first = second, first.next
            second.next, second = first, second.next