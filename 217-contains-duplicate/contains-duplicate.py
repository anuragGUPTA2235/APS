class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uni = set()
        for items in nums:
            uni.add(items)
        print(uni,len(uni))


        return len(uni) != len(nums)    
        