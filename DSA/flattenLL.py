class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def inorder(self,root) :
        global ptr
        if not root :
            return
        self.inorder(root.left)
        ptr.next = LLNode(root.val,None)
        ptr = ptr.next
        self.inorder(root.right)

    def solve(self, root):
        global ptr
        if not root :
            return
        head = LLNode(-1,None)
        ptr = head
        self.inorder(root)
        return head.next
ptr = LLNode(0)
root = Tree(2,None,None)
root.left = Tree(1,None,None)
root.right = Tree(4,None,None)
root.right.left = Tree(3,None,None)

sol = Solution()
ans = sol.solve(root)

while ans :
    print(ans.val)
    ans = ans.next
