# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def rec(n):
            if not n:
                return (0,-9999)
            val = n.val
            left = rec(n.left)
            right = rec(n.right)
            answer_left = val+max(left[0], right[0], 0)
            answer_right = max((val + max(left[0],0)+max(right[0],0)), left[1], right[1])
            
            answer = (answer_left, answer_right)
            return answer
        item = rec(root)
        return item[1]



        