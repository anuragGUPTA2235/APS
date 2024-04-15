# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        mem = []
        current = head
        while current is not None:
            mem.append(current.val)
            current = current.next
       
        indexleft = 0
        indexright = 0

        for index,items in enumerate(mem):
            if index+1 == left:
                indexleft = index
            if index+1 == right:
                indexright = index
        
        mem[indexleft:indexright+1] = mem[indexleft:indexright+1][::-1]  

        print(mem)  

        current = head
        i = 0
        while current is not None:
            current.val = mem[i]
            current = current.next    
            i += 1    

        return head         

        

