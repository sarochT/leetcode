class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = str(l1.val)
        num2 = str(l2.val)
        num3 = ""
        
        while l1.next != None:
            l1 = l1.next
            num1 = str(l1.val) + num1
        
        while l2.next != None:
            l2 = l2.next
            num2 = str(l2.val) + num2
            
        num3 = int(num1) + int(num2)
        num3 = str(num3)
        
        head = ListNode(int(num3[-1]))
        current_node = head
        
        # 807
        # 7 -> 0 -> 8
        for i in range(1, len(num3)):
            current_node.next = ListNode(num3[len(num3)-i-1])
            current_node = current_node.next
        return head