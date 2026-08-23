# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = []
        dp = {}
        def rec(n):
            if not n:
                return 0
            if n in dp:
                return dp[n]
            val = n.val
            answer.append(val+max(rec(n.left),0)+max(rec(n.right),0))
            val+= max(rec(n.left), rec(n.right), 0)
            

            dp[n] = val
            return val
        rec(root)
        return max(answer)


        