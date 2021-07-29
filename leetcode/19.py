class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ptr = head
        for i in range(1,n) :
            ptr = ptr.next
        ans = head
        prev = None
        while ptr and ptr.next :
            ptr = ptr.next
            prev = ans
            ans = ans.next
        if not prev : return head.next
        prev.next = ans.next
        return head
