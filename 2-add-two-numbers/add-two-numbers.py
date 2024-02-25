# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []
        current = l1
        while current is not None:
            print(current.val)
            arr1.append(current.val)
            current = current.next
        current = l2
        while current is not None:
            
            arr2.append(current.val)
            current = current.next          
 
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        num1 = ""
        num2 = ""
        for items in arr1:
            num1+=str(items)
        for items in arr2:
            num2+=str(items)
        print(num1,num2) 
        num1 = int(num1)
        num2 = int(num2)
        res = num1 + num2
        res = str(res)
        print(res)    
        resarr = []
        for items in res:
            resarr.append(items)
        print(resarr)
        resarr = resarr[::-1]
        for i in range(len(resarr)):
            resarr[i] = int(resarr[i])

        print(resarr)  
        node = ListNode(resarr[0])
        l1 = node
        current  = l1
        for i in range(1,len(resarr)):
            node = ListNode(resarr[i])
            current.next = node
            current = node

        return l1    
        
