class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i  in range(len(nums)):
            nums[i] = str(nums[i])
        print(nums)    

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                a = int(nums[i] + nums[j])
                b = int(nums[j] + nums[i])
                if a < b:
                    nums[i],nums[j] = nums[j],nums[i]
                
                 



        print(nums)
        return str(int("".join(nums)))           
