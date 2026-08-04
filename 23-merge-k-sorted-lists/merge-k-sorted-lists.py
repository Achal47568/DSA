# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []

        # Collect all values
        for head in lists:
            while head:
                nums.append(head.val)
                head = head.next

        # Sort all values
        nums.sort()

        # Create new linked list
        dummy = ListNode(0)
        curr = dummy

        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next