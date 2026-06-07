# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev=None
        left=head
        right=head
        for i in range(n):
            right=right.next

        while right!=None:
            prev=left
            left=left.next
            right=right.next
        if prev==None:
            return head.next
        print(prev.val)
        prev.next=left.next

        return head
        
        
        
        

        



        