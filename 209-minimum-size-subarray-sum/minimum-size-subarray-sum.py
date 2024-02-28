class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        totalsum = sum(nums)
        if target  > totalsum:
            return 0
        mini = float(inf)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                sub = nums[i:j]
                if sum(sub) >= target:
                    length = len(sub)
                    if length < mini:
                        mini = length
                        break
        return mini
        """

        minimum = float(inf)
        sum = 0
        left = 0
        for right in range(len(nums)):
            sum = sum + nums[right]
            while sum >=target:
                minimum = min(minimum,right - left + 1)
                sum -= nums[left]
                left += 1

        if minimum == float(inf):
            return 0
        else:
            return minimum           

       
        