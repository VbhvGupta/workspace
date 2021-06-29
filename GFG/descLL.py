class Solution:
    def reverse (self, head) :
        prev = None
        ptr = head
        while ptr :
            tmp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = tmp
        return prev

    def compute(self,head):
        if not head.next : return head
        head = self.reverse(head)
        ptr = head.next
        prev = head
        while ptr :
            if ptr.data < prev.data :
                prev.next = ptr.next
                ptr = ptr.next
            else :
                prev = ptr
                ptr = ptr.next
        return self.reverse(head)


#  Driver Code Starts
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
            self.tail =new_node
            return
        self.tail.next=new_node
        self.tail=new_node

    def getNode(self,value): # return node with given value, if not present return None
        curr_node=self.head
        while(curr_node.next and curr_node.data != value):
            curr_node=curr_node.next
        if(curr_node.data==value):
            return curr_node
        else:
            return None

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print(' ')

if __name__=="__main__":
    t=int(input())
    while(t>0):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)


        result=Solution().compute(a.head)
        a.head=result
        a.printList()
        t-=1
# Driver Code Ends
