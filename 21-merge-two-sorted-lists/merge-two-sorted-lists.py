# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        current = list1
        while current is not None:
            print(current.val)
            current = current.next
        current = list2
        while current is not None:
            print(current.val)
            current = current.next
        """    
        if list1 is None:
            return list2
        elif list2 is None:
            return list1    
        # travel to the last node of list1 and connect to list2
        current = list1
        prev = ListNode()
        while current is not None:
            #print("yes")
            prev = current
            current = current.next
        prev.next = list2 
        # see the merged list and sort
        current = list1
        while current is not None:
            print(current.val)
            current = current.next        



        swapped =True
        while swapped:
         swapped = False
         current = list1   
         while current is not None and current.next is not None:
            if current.val > current.next.val:
                current.val,current.next.val = current.next.val,current.val 
                swapped =True
            current = current.next  

        current = list1
        while current is not None:
            print(current.val)
            current = current.next

        return list1    



           

        
   
        