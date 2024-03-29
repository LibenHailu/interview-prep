# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def merger(l1,l2):
            if not l1:
                return l2
            elif not l2:
                return l1
            
            elif l1.val > l2.val:
                return ListNode(l2.val,merger(l1,l2.next))
            
            else:
                return ListNode(l1.val,merger(l1.next,l2))
        
        return merger(list1,list2)
        