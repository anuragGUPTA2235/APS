class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        print(target)
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    print(i,nums[j])
                    return i,j
    
        """
        list = {}
        for index,items in enumerate(nums):
            list[items] = index
        print(list)    

        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in nums[i+1:]:
                print(residual)
                return i,list[residual]  
        """                  
        