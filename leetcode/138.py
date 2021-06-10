"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head :
            return None

        if not head.next :
            new = Node(head.val)
            if head.random == head :
                new.random = new
            return new

        p1 = head
        ans = Node(-1)
        ptr = ans

        while p1 :
            new = Node(p1.val)
            new.next=p1.next
            p1.next = new
            p1 = new.next

        p1 = head

        while p1:
            if p1.random :
                p1.next.random = p1.random.next
            else :
                p1.next.random = None
            p1 = p1.next.next

        p1 = head

        while p1 and p1.next :
            ptr.next = p1.next
            p1.next = p1.next.next
            ptr = ptr.next
            p1 = p1.next

        return ans.next
