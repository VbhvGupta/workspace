# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head :
            return head
        if not head.next:
            return head
        odd_head = ListNode(-1)
        even_head = ListNode(-2)
        odd = odd_head
        even = even_head
        ptr = head
        i=1
        while ptr :
            if i:
                i=0
                odd.next = ptr
                odd = odd.next
            else :
                i=1
                even.next = ptr
                even = even.next
            ptr = ptr.next
        odd.next = even_head.next
        even.next = None
        return odd_head.next
