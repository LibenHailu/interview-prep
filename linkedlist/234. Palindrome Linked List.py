# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse(node: Optional[ListNode]):
            prev = None
            while node:
                node_next = node.next
                # node.next = None
                node.next = prev
                prev = node
                node = node_next
            
            return prev
        
        if not head.next:
            return True
        
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        tail = reverse(slow.next)
        slow.next = None
        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True
        
#         Solution.ref = head
#         self.ans = True
    
#         def rec(cur):
#             if not cur:
#                 return 

#             rec(cur.next)
            
#             if cur.val != Solution.ref.val:
#                 self.ans =  False
             
#             Solution.ref = Solution.ref.next
        
#         rec(head)
#         return self.ans   
#         return self.ans
#         dummy=None
#         current = None
#         def reverse(head):
#             nonlocal dummy
#             if not head: 
#                 return
#             reverse(head.next)


#             if not dummy:
#                 dummy = ListNode(head.val)
               
#             else:
#                 cur = dummy
#                 while cur.next:
#                     cur = cur.next
#                 cur.next = ListNode(head.val)
              
#         reverse(head)
#         print(head)
#         print(dummy)
#         return dummy == head