# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr=head 
        last=head
        prev=head 

        if head is None or head.next is None: 
            return 
        
        while(prev.next.next): 
            prev=prev.next 

        last=prev.next 
        prev.next=None
        
        
        newhead=curr.next  
        curr.next=last
        last.next=newhead

        self.reorderList(newhead)
        
