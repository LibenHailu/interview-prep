# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        h = []

        for node in lists:
            while node:
                heappush(h, node.val)
                node = node.next

        if len(h) == 0:
            return None

        start = ListNode(heappop(h))

        ans = start

        while len(h) > 0:
            ans.next = ListNode(heappop(h))
            ans = ans.next

        return start
