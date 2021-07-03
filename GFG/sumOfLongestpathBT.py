class Solution:
    def sumOfLongRootToLeafPath(self,root):
        m = {root : [root.data,1]}
        ans = [root.data,1]
        max_level = 1
        queue = [root]
        while queue :
            ptr = queue.pop(0)
            if ptr.left :
                m[ptr.left]  = [m[ptr][0]+ptr.left.data , m[ptr][1]+1]
                queue.append(ptr.left)
                if m[ptr.left][1] > max_level :
                    max_level = m[ptr.left][1]
                    ans = [m[ptr.left][0],max_level]
                elif m[ptr.left][0] > ans[0] :
                    ans[0] = m[ptr.left][0]

            if ptr.right :
                m[ptr.right] = [m[ptr][0]+ptr.right.data, m[ptr][1]+1]
                queue.append(ptr.right)
                if m[ptr.right][1] > max_level:
                    max_level = m[ptr.right][1]
                    ans = [m[ptr.right][0],max_level]
                elif m[ptr.right][0] > ans[0] :
                    ans[0] = m[ptr.right][0]

        return ans[0]

#{
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip=list(map(str,s.split()))

    # Create the root of the tree
    root=Node(int(ip[0]))
    size=0
    q=deque()

    # Push the root to the queue
    q.append(root)
    size=size+1

    # Starting from the second element
    i=1
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1

        # Get the current node's value from the string
        currVal=ip[i]

        # If the left child is not null
        if(currVal!="N"):

            # Create the left child for the current node
            currNode.left=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]

        # If the right child is not null
        if(currVal!="N"):

            # Create the right child for the current node
            currNode.right=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s=input()
        root=buildTree(s)
        ob = Solution()
        res = ob.sumOfLongRootToLeafPath(root)
        print(res)
# } Driver Code Ends
