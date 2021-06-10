def buildTree2( preorder, inorder) :
    ln = len(inorder)
    if ln == 0 :
        return None
    if ln == 1:
        return TreeNode(inorder[0],None,None)

    root = TreeNode(preorder[0],None,None)
    mid = inorder.index(root.val)

    if mid !=0  and mid != ln-1 :
        root.left = buildTree2( preorder[1:mid+1], inorder[:mid] )
        root.right = buildTree2(preorder[mid+1:] , inorder[mid+1: ] )
    elif mid != 0 :
        root.left = buildTree2(preorder[1:] , inorder[:mid])
        root.right = None
    elif mid != ln-1 :
        root.left = None
        root.right = buildTree2(preorder[mid+1:] , inorder[mid+1:])
    else :
        return None
    return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = buildTree2( preorder,inorder)
        return root
