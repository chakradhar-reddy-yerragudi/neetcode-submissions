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
        hmapNO={}
        hmapNO[None]=None
        old=head
        while old:
            new.next=Node(old.val)
            hmapON[old]=new.next
            hmapNO[new.next]=old
            new=new.next
            old=old.next
        new=dummy.next
        while new:
            new.random=hmapON[hmapNO[new].random]
            new=new.next
        return dummy.next
            
        



        