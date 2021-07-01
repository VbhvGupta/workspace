# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def tree2str(self, root: TreeNode) -> str:
        if not root : return
        ans = ''
        def preorder(root) :
            nonlocal ans
            if not root : return
            ans += str(root.val)
            if not root.left and not root.right : return
            if root.left :
                ans+='('
                preorder(root.left)
                ans+=')'
            else :
                ans+='()'
            if root.right :
                ans+='('
                preorder(root.right)
                ans+=')'
            return
        preorder(root)
        return ans
