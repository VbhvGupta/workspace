# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = [root]
        cur = 0
        ans = []

        def left2right(queue):
            temp = []
            for_ans = []
            while queue:
                ptr = queue.pop(0)
                for_ans.append(ptr.val)
                if ptr.left :
                    temp.append(ptr.left)
                if ptr.right:
                    temp.append(ptr.right)
            ans.append(for_ans)
            return temp

        def right2left(queue):
            temp = []
            for_ans = []
            while queue:
                ptr = queue.pop(0)
                for_ans.append(ptr.val)
                if ptr.left :
                    temp.append(ptr.left)
                if ptr.right:
                    temp.append(ptr.right)
            ans.append(for_ans[::-1])
            return temp

        while queue :
            if cur == 0:
                queue = left2right(queue)
            else :
                queue = right2left(queue)
            cur = not(cur)
        return ans
