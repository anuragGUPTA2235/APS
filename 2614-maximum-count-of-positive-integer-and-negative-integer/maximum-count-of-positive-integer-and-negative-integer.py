class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos_count = 0
        neg_count = 0
        for index,items in enumerate(nums):
            if items > 0:
                pos_count += 1
            elif items < 0:
                neg_count += 1
        return max(pos_count,neg_count)            

        