import math
class Solution:
    def splitList(self, head, head1, head2):
        #code here
        if not head or not head.next :
            return
        ln = 1
        last = head
        while last.next != head :
            ln+=1
            last = last.next
        head1 = head
        ln = math.ceil(ln/2)
        i=1
        ptr2 = head
        while i<ln :
            ptr2=ptr2.next
            i+=1
        head2 = ptr2.next
        last.next = head2
        ptr2.next = head

        return head1,head2

#  Driver Code Starts
class Node:
    def __init__(self):
        self.data = None
        self.next = None

def printCircularLinkedList(head):
    tmp = head
    while True:
        print(tmp.data, end = " ")
        tmp = tmp.next
        if tmp == head:
            break
    print()

if __name__ == "__main__":
    for i in range(int(input())):
        head = Node()
        head1 = Node()
        head2 = Node()
        tmp = head
        n = int(input())
        for i in input().split():
            tmp.next = Node()
            tmp = tmp.next
            tmp.data = int(i)
        head = head.next
        tmp.next = head
        obj = Solution()
        head1,head2 = obj.splitList(head,head1,head2)
        printCircularLinkedList(head1)
        printCircularLinkedList(head2)

# Driver Code Ends
