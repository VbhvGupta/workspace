class Solution:
    def merge(self, left, right):
        head = Node(-999999)
        ptr = head
        while left and right :
            if left.data < right.data :
                ptr.next = left
                left = left.next
            else :
                ptr.next = right
                right = right.next
            ptr = ptr.next

        if left :
            ptr.next = left
        else :
            ptr.next = right

        return head.next

    def mergeSort(self, head):
        if head.next is None :
            return head
        mid = head
        slow = head
        fast = head
        while fast and fast.next :
            mid = slow
            slow = slow.next
            fast = fast.next.next
        mid.next = None

        left = self.mergeSort(head)
        right = self.mergeSort(slow)

        return self.merge(left, right)




#{
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends
