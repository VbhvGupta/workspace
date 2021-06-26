#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

def reverseDLL(head):
    if not head or not head.next :
        return head
    prev = None
    cur = head
    while cur :
        tmp = cur.next
        cur.next = prev
        cur.prev = tmp
        prev = cur
        cur = tmp
    return prev



# Driver code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data,tail):
        if not self.head:
            self.head=Node(new_data)
            return self.head
        Nnode=Node(new_data)
        Nnode.prev=tail
        tail.next=Nnode
        return Nnode

    def printList(self, node):
        while(node is not None):
            print (node.data,end=' ')
            node = node.next



if __name__ == '__main__':
    t=int(input())

    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]


        dll=DoublyLinkedList()
        tail=None

        for e in arr:
            tail=dll.push(e,tail)

        resHead=reverseDLL(dll.head)
        dll.printList(resHead)
        print()

# Driver Code Ends
