class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """ 
        brute force
        prod = 1
        counter = 0

        for i in range(len(nums)):
            prod = nums[i]
            if nums[i] < k:
                counter += 1
            for j in range(i+1,len(nums)):
                prod = prod * nums[j]
                if prod < k:
                    counter += 1
                elif prod >= k:
                    break     
        
        return counter
        """

        left = 0
        prod = 1
        count = 0

        if k <= 1:
            return  0

        for right,items in enumerate(nums):
            prod = prod * nums[right]
            while prod >= k:
                prod = prod / nums[left]
                left += 1

            count += right -left + 1

        return count    
        


        