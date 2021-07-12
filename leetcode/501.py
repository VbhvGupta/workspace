# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        dct = {}
        def inorder(root) :
            nonlocal dct
            if not root :
                return
            inorder(root.left)
            if root.val not in dct :
                dct[root.val] = 0
            dct[root.val] += 1
            inorder(root.right)
        inorder(root)
        max_ = 0
        for key in dct :
            if dct[key] > max_ :
                max_ = dct[key]
        ans = []
        for key in dct :
            if max_ == dct[key] :
                ans.append(key)
        return ans
