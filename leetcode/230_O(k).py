# O(K) TC, O(1) SC
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = None
        count = 0
        def inorder(root,k) :
            nonlocal ans
            nonlocal count
            if ans : return
            if not root :
                return
            inorder(root.left,k)
            count += 1
            if count == k :
                ans = root
            inorder(root.right,k)
        inorder(root,k)
        return ans.val
