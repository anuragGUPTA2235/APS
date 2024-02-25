class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         i = 0
         while i < len(nums):
             current = nums[i]
             if nums.count(current)>1:
                 nums.remove(current)
             else:
                 i+=1
         print(nums)        
                 


        