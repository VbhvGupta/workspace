# O(n) TC, O(n) SC
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
