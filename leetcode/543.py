# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def diameterOfBT(self, root) :
        if not root : return 0
        left_h = self.diameterOfBT(root.left)
        right_h = self.diameterOfBT(root.right)
        if left_h + right_h + 1 > self.diameter :
            self.diameter = left_h + right_h + 1
        return max(left_h,right_h)+1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameterOfBT(root)
        return self.diameter-1


        
