# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        curr=head 
        if head is None: 
            return 
        
        while(curr): 
            length+=1 
            curr=curr.next 

        remove_index=length-n 
        dummy=head
        prev=head
        nxt=head.next 
        tracker=0
        if head.next is None and n==1: 
            return
        
        
        while(nxt): 
            if(remove_index==0): 
                return nxt
            tracker+=1 
            if(tracker==remove_index): 
                temp= nxt.next
                nxt.next=None
                prev.next=temp
                break
            else: 
                nxt=nxt.next 
                prev=prev.next 
        return dummy

        