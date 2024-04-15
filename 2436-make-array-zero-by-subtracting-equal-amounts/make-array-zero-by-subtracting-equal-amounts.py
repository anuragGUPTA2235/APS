class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        summation = sum(nums)
        tracker = 0
        print(nums)

        if len(nums) == 1 and nums[0]==0:
            return 0
        if len(nums) ==  1 and nums[0] != 0:
            return 1    
        while summation != 0 :
            for i in range(0,len(nums)):
                if nums[i] != 0:
                    second_minimum = nums[i]
                    break

            for i in range(len(nums)):
                if nums[i] != 0:
                 nums[i] -= second_minimum
            summation  = sum(nums)  
            nums.sort()  
            print(nums)
            tracker += 1

        return tracker    


        