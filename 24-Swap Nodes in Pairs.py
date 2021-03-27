# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        # 0 node in list
        if head is None:
            return None

        # 1 node in list
        if head.next is None:
            return head
        
        
        current_node = head
        next_node = head.next
        # if there's more than 2 nodes in list, 
        # head node will be the second node in list
        head = next_node
        
        # first move
        current_node.next = next_node.next
        next_node.next = current_node
        
        while current_node.next is not None and current_node.next.next is not None:
            previous_node = current_node
            current_node = current_node.next
            next_node = current_node.next
            
            previous_node.next = next_node
            current_node.next = next_node.next
            next_node.next = current_node
            
        return head
