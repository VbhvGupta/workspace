#User function Template for python3
'''
	Your task is to merge the given k sorted
	linked lists into one list and return
	the the new formed linked list class.

	Function Arguments:
	    arr is a list containing the n linkedlist head pointers
	    n is an integer value

    node class:

class Node:
    def __init__(self,x):
        self.data = x
        self.nxt = None
'''
class Solution:
    def merge(self,left,right) :
        head = Node(-1)
        merged = head
        while left and right :
            if left.data < right.data :
                merged.next = left
                left = left.next
            else :
                merged.next = right
                right = right.next
            merged = merged.next
        if left :
            merged.next = left
        else :
            merged.next = right
        return head.next

    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        # code here
        if K == 1 : return arr[0]
        mid = K//2
        left = self.mergeKLists(arr[:mid],mid)
        right = self.mergeKLists(arr[mid:],K-mid)
        return self.merge(left,right)


#{
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next

def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]

        heads=[]
        index=0

        for i in range(n):
            size=line[index]
            index+=1

            newList = LinkedList()

            for _ in range(size):
                newList.add(line[index])
                index+=1

            heads.append(newList.head)

        merged_list = Solution().mergeKLists(heads,n)
        printList(merged_list)

# } Driver Code Ends
