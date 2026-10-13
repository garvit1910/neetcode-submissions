# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode()
        head=list3
        while True:
            if list1 is None and list2 is None: 
                return head.next
            elif list1 is None and list2 is not None: 
                list3.next=list2 
                break
            elif list2 is None and list1 is not None: 
                list3.next=list1
                break
            if(list1.val <= list2.val): 
                list3.next=list1 
                list1=list1.next 
                list3=list3.next 
            else: 
                list3.next=list2 
                list2=list2.next 
                list3=list3.next 
        
        return head.next
