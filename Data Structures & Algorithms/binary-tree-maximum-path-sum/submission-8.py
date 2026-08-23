# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = [root.val]
        def rec(n):
            if not n:
                return 0
            val = n.val
            left = rec(n.left)
            right = rec(n.right)
            answer[0] = max(answer[0],(val+max(left,0)+max(right,0)))
            val+= max(left, right, 0)
            return val
        rec(root)
        return answer[0]


        