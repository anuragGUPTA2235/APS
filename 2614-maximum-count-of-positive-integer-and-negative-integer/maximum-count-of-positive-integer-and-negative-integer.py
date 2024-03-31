class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """
        pos_count = 0
        neg_count = 0
        for index,items in enumerate(nums):
            if items > 0:
                pos_count += 1                  
            elif items < 0:
                neg_count += 1
        return max(pos_count,neg_count) 
        """
        # efficient way
        # use binary search

        def pos_num(nums):
            arr = nums
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) //  2
                if nums[mid] > 0:
                    right = mid - 1
                else:
                    left = mid + 1
            return len(arr) - right - 1  

        def neg_num(nums):
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left + right) // 2 
                if nums[mid] < 0:
                    left = mid + 1
                else:
                    right = mid - 1
            return left                 
        
        p = pos_num(nums)
        n = neg_num(nums)
        if p > n:
            return p
        else:
            return n          





        