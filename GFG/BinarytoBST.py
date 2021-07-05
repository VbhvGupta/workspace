class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST(self, root):
        arr = []
        def inorder(root) :
            nonlocal arr
            if not root :
                return
            inorder(root.left)
            arr.append(root.data)
            inorder(root.right)
        inorder(root)
        arr = sorted(arr)
        def tree(root) :
            nonlocal arr
            if not root :
               return
            tree(root.left)
            root.data = arr.pop(0)
            tree(root.right)
        tree(root)
        return root
