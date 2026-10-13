# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow,fast= head, head 
        if(head is None or head.next is None): 
            return False
        while head:
            if fast.next is None or fast.next.next is None: 
                return False
            fast=fast.next.next 
            slow=slow.next 
            head=head.next 

            if(slow==fast): 
                return True 
        
        
        return False
        