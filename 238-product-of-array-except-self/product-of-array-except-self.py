class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ O(n2)
        list = []
        for i in range(len(nums)):
            mul = 1
            nums[0],nums[i] = nums[i],nums[0]
            for j in range(1,len(nums)):
                mul = mul * nums[j]
            list.append(mul)

        print(list)   
        return list  
        """   
        # optimized one
        left = [1]*len(nums)
        right = [1]*len(nums)
        for i in range(1,len(nums)):
            left[i] = nums[i-1] * left[i-1]
        print(left)    
        for i in range(len(nums)-2,-1,-1):
            print(i)
            right[i] = nums[i+1] * right[i+1]
        print(right)   
        for i in range(len(nums)):
            left[i] = left[i] * right[i]
        return left          

  
        