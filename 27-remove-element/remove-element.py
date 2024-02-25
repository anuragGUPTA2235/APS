class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        k = 0
        for items in nums:
            if items != val:
                k+=1
        print(k) 
        print(len(nums)-k)
        counter = len(nums)-k
        while counter!=0:
             nums.remove(val)
             counter -= 1



        