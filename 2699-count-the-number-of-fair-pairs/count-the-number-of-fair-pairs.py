
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:


        counter = 0
        nums.sort()

        for i in range(len(nums)):

            bisectleft = bisect_left(nums,lower-nums[i],i+1,len(nums))
            bisectright = bisect_right(nums,upper-nums[i],i+1,len(nums))

     
            counter += (bisectright - bisectleft) 

    



        return counter

        