class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        list = []
        for items in range(0,n+1):
            list.append(items)

        for items in list:
            if items not in nums:
                return items


     
        