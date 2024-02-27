class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        indexlist = []
        k = k % len(nums)
        for index,item in enumerate(nums):
            indexlist.append((index+k)%len(nums))
        print(indexlist)    

        tempo = nums.copy()
        for i in range(len(nums)):
            nums[indexlist[i]] = tempo[i]    
        