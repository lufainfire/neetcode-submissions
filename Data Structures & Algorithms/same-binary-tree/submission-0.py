# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def type(node: OptionalTreeNode) -> int:
            if not node:
                return 0
            if not node.right and not node.left:
                return 2
            elif not node.left:
                return 4
            elif not node.right:
                return 3
            else:
                return 1

        num_p = type(p)
        num_q = type(q)
        #base case
        if num_p != num_q:
            return False
        elif num_p == 0:
            return True
        elif p.val != q.val:
            return False
        # no child
        elif num_p == 2:
            return True
        # two child
        elif num_p == 1:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        # left child
        elif num_p == 3:
            return self.isSameTree(p.left,q.left)
        #right child 
        else:
            return self.isSameTree(p.right,q.right)
