class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while True:
            smallest_idx = -1
            # find the list whose current head is the smallest
            for i, node in enumerate(lists):
                if node is not None:
                    if smallest_idx == -1 or node.val < lists[smallest_idx].val:
                        smallest_idx = i

            if smallest_idx == -1:      # all lists exhausted
                break

            tail.next = lists[smallest_idx]          # attach smallest node
            tail = tail.next
            lists[smallest_idx] = lists[smallest_idx].next  # advance that list

        return dummy.next