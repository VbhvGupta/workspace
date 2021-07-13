def countPairs(root1, root2, x):
    if not root1 or not root2 :
        return 0

    count = 0
    s1,s2 = [],[]

    ptr1 = root1
    ptr2 = root2
    while True :

        while ptr1 :
            s1.append(ptr1)
            ptr1 = ptr1.left

        while ptr2 :
            s2.append(ptr2)
            ptr2= ptr2.right

        if not s1 or not s2 :
            return count

        l,r = s1[-1],s2[-1]
        if l.data + r.data < x :
            s1.pop()
            if l.right :
                ptr1 = l.right

        elif l.data + r.data > x:
            s2.pop()
            if r.left :
                ptr2 = r.left

        else :
            count += 1
            s1.pop()
            s2.pop()
            if l.right :
                ptr1 = l.right
            if r.left :
                ptr2 = r.left



#{
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def insert(root, node):
    if root == None:
        root = node
    else:
        if (root.data < node.data):
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)
        elif (root.data > node.data):
            if (root.left == None):
                root.left = node
            else:
                insert(root.left, node)

if __name__ == "__main__":
    t = int(input())
    while t>0:
        n1 = int(input())
        list = [int(x) for x in input().strip().split()]
        root1=Node(list[0])
        for i in range(1, n1):
            insert(root1, Node(list[i]))

        n2 = int(input())
        list = [int(x) for x in input().strip().split()]
        root2 = Node(list[0])
        for i in range(1, n2):
            insert(root2, Node(list[i]))
        s = int(input())
        print(countPairs(root1, root2, s))
        t=t-1

# } Driver Code Ends
