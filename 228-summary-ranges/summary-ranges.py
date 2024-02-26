class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        list = []
        while i < len(nums):
            begin = nums[i]
            while i < len(nums)-1 and nums[i+1] - nums[i]==1:
                i = i+1
            end = nums[i]
            if begin == end:
                list.append(str(begin))
            else:
                list.append(str(begin)+"->"+str(end))  
            i = i+1
        return list

        