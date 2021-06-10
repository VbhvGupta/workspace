class Solution:
    def merge(self , left :ListNode , right : ListNode) -> ListNode :
        p1 , p2 = left , right
        head = ListNode(0,None)
        temp = head
        while p1 and p2 :
            if p1.val <= p2.val :
                temp.next = p1
                p1 = p1.next
            else :
                temp.next = p2
                p2 = p2.next
            temp = temp.next
        if p1 :
            temp.next = p1
        elif p2 :
            temp.next = p2
        return head.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next :
            return head
        slow , fast , mid = head , head , None

        while fast != None and fast.next != None :
            mid = slow
            slow = slow.next
            fast = fast.next.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left,right)
