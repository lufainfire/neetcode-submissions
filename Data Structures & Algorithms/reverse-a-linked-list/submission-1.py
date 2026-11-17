# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        curr = head
        prev = None
        while curr:
            temp = ListNode(curr.val,prev)
            curr = curr.next
            prev = temp
        return prev

            


            

        
        