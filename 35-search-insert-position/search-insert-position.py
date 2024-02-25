class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        print(nums)
        print(target)

        if target > max(nums):
            return len(nums)
        if target < min(nums):
            return 0  
        for index,items in enumerate(nums):
            if items == target:
                return index
            elif target < max(nums):
                for i in range(len(nums)-1):
                    if nums[i]<target and nums[i+1]>target:
                        return i+1
            
                  


    
        