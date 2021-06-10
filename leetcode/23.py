# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self , left , right) :
        head = ListNode()
        temp = head
        while left and right :
            if left.val <= right.val :
                temp.next = left
                left = left.next
            else :
                temp.next = right
                right = right.next
            temp = temp.next

        if left :
            temp.next = left
        elif right :
            temp.next = right
        return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ln = len(lists)
        if ln == 0  :
            return None
        if ln == 1:
            return lists[0]

        mid = len(lists)//2

        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left,right)
