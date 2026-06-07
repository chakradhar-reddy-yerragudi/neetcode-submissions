# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow=head
        fast=head.next


        while fast and fast.next:
 


            slow=slow.next
            fast=fast.next.next
       



      
        prev=None
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
     

        
        while prev and head:
            temp1,temp2=head.next,prev.next
            head.next=prev
            prev.next=temp1
            head=temp1
            prev=temp2
        

        
        
        
   



\



        
        




        


        



        












        



        