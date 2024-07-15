# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(None)
        orig = res
        def collectValues(start):
            values = []
            while start and start.val != 0:
                values.append(start.val)
                start = start.next
            return (values, start)
        cursor = head
        # disregard the zeroes and only collect in between
        while cursor and cursor.next:
            values, nxt = collectValues(cursor.next)
            res.next = (ListNode(sum(values)))
            res = res.next
            cursor = nxt
        return orig.next
        