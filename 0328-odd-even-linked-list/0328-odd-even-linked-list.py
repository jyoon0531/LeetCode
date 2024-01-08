# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        oddNode = ListNode()
        odd = oddNode
        evenNode = ListNode()
        even = evenNode

        order = 0
        while head:
            order += 1
            if order % 2 == 0:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            head = head.next

        even.next = None
        odd.next = evenNode.next

        return oddNode.next

