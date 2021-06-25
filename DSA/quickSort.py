#User function Template for python3

def partition(start,end) :
    begin = start
    pivot = begin.data
    cur = start
    prev = cur
    p_prev = prev
    while start and end and start != end :

        while start and start.data <= pivot :
            start = start.next
            p_prev = prev
            prev = cur
            cur = cur.next

        while start and start.data > pivot :
            start = start.next

        if start and cur.data > start.data:
            temp = cur.data
            cur.data = start.data
            start.data = temp
            p_prev = prev
            prev = cur
            cur = cur.next

    tmp = prev.data
    prev.data = pivot
    begin.data = tmp

    return p_prev,cur



def qsort(start,end) :
    if start == end :
        return start

    left_end,right_start = partition(start,end)

    if start and left_end and start != left_end :
        qsort(start,left_end)
    if right_start and end and right_start != end :
        qsort(right_start,end)

    return start

def quickSort(head):
    end = head
    while end.next :
        end = end.next
    return qsort(head,end)

#{
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None

    def insert(self,data,tail):
        node=Node(data)

        if not self.head:
            self.head=node
            return node

        tail.next=node
        return node

def nodeID(head,dic):
    while head:
        dic[head.data].append(id(head))
        head=head.next



def printList(head,dic):
    while head:
        # if id(head) not in dic[head.data]:
        #     pass
        #     #print("Do'nt swap data, swap pointer/node")
        #     return
        print(head.data,end=' ')
        head=head.next

if __name__ == '__main__':
    t=int(input())

    for tcs in range(t):
        n=int(input())

        arr=[int(x) for x in input().split()]

        ll=Llist()
        tail=None

        for nodeData in arr:
            tail=ll.insert(nodeData,tail)

        dic=defaultdict(list)   # dictonary to keep data and id of node
        nodeID(ll.head,dic)     # putting data and its id

        resHead=quickSort(ll.head)
        printList(resHead,dic)  #verifying and printing
        print()



# } Driver Code Ends
