# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        sublist = []
        stack = []
        if root != None:
            stack.append([root,0])
        level = -1
    
        
        while stack != []:
            node_tuple = stack.pop(0)
            ptr = node_tuple[0]
            lvl = node_tuple[1]

            if level != lvl-1:
                answer.append(sublist)
                sublist=[]
                level+=1

            if ptr.left != None:
                stack.append([ptr.left, lvl+1])
            if ptr.right != None:
                stack.append([ptr.right,lvl+1])
            sublist.append(ptr.val)
        if sublist != []:
            answer.append(sublist)
        return answer


            
        