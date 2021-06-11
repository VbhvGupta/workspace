# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder_(self,root,lst) :
        if not root:
            return
        self.inorder_(root.left,lst)
        lst.append(root.val)
        self.inorder_(root.right,lst)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        lst = []
        self.inorder_(root,lst)
        return lst[k-1]
