# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(-1,None)
        ptr = head

        while l1 and l2 :
            sum_ = l1.val + l2.val + carry
            if sum_ > 9 :
                sum_ -= 10
                carry = 1
            else :
                carry = 0
            ptr.next = ListNode(sum_,None)
            ptr = ptr.next
            l1,l2=l1.next,l2.next

        if l1 :
            while carry and l1 :
                sum_ = l1.val + carry
                if sum_ > 9 :
                    sum_ -= 10
                    carry = 1
                else :
                    carry = 0
                ptr.next = ListNode(sum_ , None)
                l1 = l1.next
                ptr = ptr.next
            if l1 :
                ptr.next = l1
                ptr = ptr.next
            elif carry :
                ptr.next = ListNode(1,None)

        else :
            while carry and l2 :
                sum_ = l2.val+ carry
                if sum_ > 9 :
                    sum_ -= 10
                    carry = 1
                else :
                    carry = 0
                ptr.next = ListNode( sum_ , None)
                l2 = l2.next
                ptr = ptr.next
            if l2 :
                ptr.next = l2
                ptr = ptr.next
            elif carry :
                ptr.next = ListNode(1,None)
        return head.next
    
