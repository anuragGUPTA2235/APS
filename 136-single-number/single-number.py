class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for index,items in enumerate(nums):
            hashmap[items] = 0
          

        for index,items in enumerate(nums):
            hashmap[items] += 1

        print(hashmap)     
            
        min = 9000
        for index,items in enumerate(hashmap):
            if hashmap[items] < min:
                min = hashmap[items]    

        print(min)

        for index,items in enumerate(hashmap):
            if hashmap[items] == min:
                return items
        
        