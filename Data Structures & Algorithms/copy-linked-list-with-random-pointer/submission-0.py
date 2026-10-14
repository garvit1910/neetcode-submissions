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
        
        copylist=Node(0)
        dummy=copylist
        curr=head
        while(curr): 
            newnode=Node(0)
            newnode.val=curr.val 
            copylist.next=newnode 
            curr=curr.next 
            copylist=copylist.next 

        copies= { }
        original=head 
        copy= dummy.next 

        while original and copy: 
            copies[original]=copy 
            original=original.next 
            copy=copy.next 
        
        original,copy =head, dummy.next

        while original: 
            if original.random: 
                copy.random=copies[original.random]
            else: 
                copy.random=None 
            
            original=original.next 
            copy=copy.next 
        
        return dummy.next











