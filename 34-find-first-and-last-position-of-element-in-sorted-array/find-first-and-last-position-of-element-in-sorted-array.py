class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        indexlist = []
        if target not in nums:
            return [-1,-1]
        for index,items in enumerate(nums):
            if items == target:
                indexlist.append(index)
                break
        nums = nums[::-1]
        for index,items in enumerate(nums):
            if items == target:
                indexlist.append(len(nums)-1-index)  
                break       
        return indexlist             

                

        