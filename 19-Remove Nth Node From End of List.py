# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        nodes = [head]
        current = head
        while current.next is not None:
            current = current.next
            nodes.append(current)
            
            
        if n == 1:
            if len(nodes) == 1:
                return None
            if len(nodes) >= 1:
                nodes[len(nodes) - n - 1].next = None
                return head
            
        if len(nodes) - n == 0:
            return head.next
        
        before = nodes[ len(nodes) - n - 1 ]
        after = nodes[ len(nodes) - n + 1]
        before.next = after
        del nodes[ len(nodes) - n ]
        
        return head
