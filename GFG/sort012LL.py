class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        if not head or not head.next :
            return head
        zero_head = Node(-1)
        one_head = Node(-1)
        two_head = Node(-1)
        zero = zero_head
        one = one_head
        two = two_head
        ptr = head
        while ptr :
            if ptr.data == 0:
                zero.next = ptr
                zero = zero.next
            elif ptr.data == 1:
                one.next = ptr
                one = one.next
            else :
                two.next = ptr
                two = two.next
            ptr = ptr.next

        if one_head.next :
            zero.next = one_head.next
            one.next = two_head.next
        else :
            zero.next = two_head.next
        two.next = None
        head = zero_head.next
        return head


#  Driver Code Starts

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
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
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        printList(Solution().segregate(a.head))
# Driver Code Ends
