class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for index,items in enumerate(nums):
            hashmap[items] = 0
          

        for index,items in enumerate(nums):
            hashmap[items] += 1

        print(hashmap)     
            

        for index,items in enumerate(hashmap):
            if hashmap[items] == 1:
                return items
        
        