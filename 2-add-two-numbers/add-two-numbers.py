# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 = 0  #convert list in n1 and n2
        p = 1   #place vales such as (10,100,1000..etc)
        while l1:
            n1 += l1.val*p  # n1 = 2x1+4x10+3x100 = 342
            p*=10          
            l1 = l1.next    #moves to next node

        p = 1
        while l2:
            n1 += l2.val*p  
            p*=10            # n2 = 5x1+6x10+4x100 = 465
            l2 = l2.next     #moves to next node

        total = n1 + n2

        dummy = ListNode(0)   #temoporary starting node
        curr = dummy          #add new nodes

        if total == 0:
            return dummy

        while total:
            curr.next = ListNode(total % 10)
            curr = curr.next
            total //= 10
        
        return dummy.next

""" 
for last while loop:
total = 342+465 = 807

807 % 10 = 7  ->add 7
807 // = 80

80 % 10 = 0  -> add 0
80 // 10 = 8

8 % 10 = 8  -> add 8
8 // 10 = 0

s0, 7->0->8

return dummy.next = returns the actual  answer
"""