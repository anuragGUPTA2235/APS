class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        print(target)
        """ brute force
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
        dic = {}
        for index,items in enumerate(nums):
            dic[items] = index
        nums.sort()
        print(nums)
        left  = 0 
        right  = len(nums)-1
        for i in range(len(nums)):
            if nums[left] + nums[right] >  target:
                right  = right - 1
            elif nums[left] +  nums[right] < target:
                left = left + 1
            else:
                return dic[nums[left]],dic[nums[right]]  
        """                         
        