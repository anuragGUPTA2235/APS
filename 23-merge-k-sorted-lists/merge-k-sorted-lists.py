# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        global temp
        temp = ListNode()
        counter = 0 
        track = 0
        for head in lists:
            if head is None:
                lists.pop(track)
            track += 1    

        if len(lists) != 0:

        
           for i in lists:
            if counter != 0:
             temp.next = i
            current = i
            while current != None:
                print(current.val)

                temp = current
                current = current.next
            counter += 1    
           print(current) 
           
           current = lists[0]
           while current is not None:
                print(current.val)
                current = current.next
            

           # now we have a unsorted merged list
           # lets sort it
           swapped =  True
           while swapped:
            swapped = False
            current = lists[0]
            while current is  not None and current.next is not None:
                if current.val > current.next.val:
                    current.val,current.next.val = current.next.val,current.val
                    swapped =  True
                current = current.next
           print()
           current = lists[0]
           while current is not None:
                print(current.val)
                current = current.next        

           return lists[0]                 

           

            
             

             
            


            

        