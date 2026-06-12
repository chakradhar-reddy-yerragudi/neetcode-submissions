"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy=Node(0)
        new=dummy
        hmapON={}
        hmapON[None]=None
        old=head
        while old:
            new.next=Node(old.val)
            hmapON[old]=new.next
            new=new.next
            old=old.next
        old=head
        while old:
            hmapON[old].random=hmapON[old.random]
            old=old.next
        return dummy.next
            
        



        