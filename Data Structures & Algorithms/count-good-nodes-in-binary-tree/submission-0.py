# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, node: TreeNode, count) -> int:
        if node == None:
            return 0
        elif count > node.val: #not good
            return self.helper(node.left, count) + self.helper(node.right, count)
        else:
            return self.helper(node.left, node.val) + self.helper(node.right, node.val) + 1
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, -999999)
        
        