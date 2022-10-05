# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = dummy = ListNode(0)
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        
        for num in sorted(nodes):
            dummy.next = ListNode(num)
            dummy  = dummy.next
        
        return head.next
            
        