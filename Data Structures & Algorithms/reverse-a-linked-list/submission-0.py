# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next
        i = len(l)-1
        l.reverse()
        prev =None
        while i >=0:
            prev = ListNode(l[i],prev)
            i-=1
        return prev


            

        
        