# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ## brute force
        ### add all items to list, disregard LL structure
        ### add back to list
        ### done
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()
        dummy = curr = ListNode(0)
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next
        return dummy.next

        
        