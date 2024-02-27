class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            current = nums[i]
            if nums.count(current)>2:
                nums.remove(nums[i])
            else:
                i+=1

        