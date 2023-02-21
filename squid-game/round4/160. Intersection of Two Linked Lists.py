# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLen(node):
            count = 0
            while node:
                count += 1
                node = node.next
            
            return count
        
        l1,l2 = getLen(headA),getLen(headB)
        longer = headA if l1 > l2 else headB
        shorter = headB if l1 > l2 else headA
        
        for _ in range(abs(l2 - l1)):
            longer = longer.next
        
        while shorter != longer:
            shorter = shorter.next
            longer = longer.next
        
        return shorter