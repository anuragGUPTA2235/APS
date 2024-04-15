# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res  = ""

        current = head
        while current is not None:
            res = res + str(current.val)
            current = current.next

        print(res)

        palin = ""

        current1 = head
        prev  = None
        while current1 != None:
            nextnode = current1.next
            current1.next = prev
            prev = current1
            current1 = nextnode

        while prev is not None:
            palin  = palin + str(prev.val)
            prev = prev.next 

        print(palin)       


        return palin == res
        