# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root : return 0
        stack = []
        stack.append([root])
        ans = 1
        while stack :
            temp_l = []
            while stack[0] :
                ptr = stack[0][0]
                if ptr.left : temp_l.append(ptr.left)
                if ptr.right : temp_l.append(ptr.right)
                stack[0].pop(0)
            stack.pop(0)
            if not temp_l : break
            ans+=1
            stack.append(temp_l)

        return ans
